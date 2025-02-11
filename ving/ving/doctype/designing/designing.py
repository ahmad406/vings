# Copyright (c) 2024, GKT and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from collections import defaultdict


class Designing(Document):
	def validate(self):
		self.fill_bill()
		# self.get_totals()
		self.calculate_final()
		self.calculate_low_side()


	def calculate_final(self):
		if not self.designing_total:
			frappe.throw("Designing Total Is Mandatory")
		for d in self.designing_total:

			if not  d.max_capacity:
				frappe.throw("Max Capacity missing in row {}".format(d.idx))
			if d.max_capacity <= 0:
				frappe.throw("Max Capacity cant be equal or less then 0  in row {}".format(d.idx))
			else:
				d.odu_capacity=d.max_capacity*25
				d.diversity =d.total_capacity_index/d.odu_capacity



	@frappe.whitelist()
	def get_totals(self):
		floor_totals = defaultdict(lambda: {"capacity": 0, "qty": 0, "total_tr": 0, "tr": 0})

		for item in self.equipment:
			item.tr = float(item.get("tr", 0))
			item.capacity = float(item.get("capacity", 0))
			floor = item.get("floor")
			floor_totals[floor]["capacity"] += item.get("capacity", 0)
			floor_totals[floor]["qty"] += item.get("qty", 0)
			floor_totals[floor]["tr"] += item.get("tr", 0)
			floor_totals[floor]["total_tr"] += float(item.get("total_tr", 0))


		self.designing_total=[]

		for floor, totals in floor_totals.items():
			
			row=self.append("designing_total",{})
			row.floor=floor
			row.total_capacity_index=totals['capacity']*totals['qty']  
			row.total_tr=totals['total_tr']
			row.total_hp= row.total_capacity_index/2
			row.total_qty=totals['qty']  
			row.hp=row.total_hp*1.25
			


	def fill_bill(self):
		data=self.sum_item()
		if data:
			for d in data:
				if not self.item_already_in(d.get("item_code")):
					row=self.append("bill_of_quantity",{})
					row.item_code=d.get("item_code")
					row.quantity=d.get("qty")
					row.unit=frappe.db.get_value('Item', d.get("item_code"), 'stock_uom')
					row.rate=get_item_price(d.get("item_code"),"Standard Selling")
					row.amount=row.rate*row.quantity

	@frappe.whitelist()
	def calculate_low_side(self):
		for d in self.designing_low_side:
			d.rate=get_item_price(d.get("item_code"),"Standard Selling")
			if d.rate and d.quantity:
				d.amount=d.quantity*d.rate

				
	def item_already_in(self,item):
		status=False
		for d in self.bill_of_quantity:
			if d.item_code==item:
				status=True
		return status

	def sum_item(self):
		item_totals = {}

		for item in self.equipment:
			code = item.get("item_code")
			qty = item.get("qty")
			
			if code in item_totals:
				item_totals[code] += qty
			else:
				item_totals[code] = qty

		return [{"item_code": code, "qty": total_qty} for code, total_qty in item_totals.items()]



def get_item_price(item_code, price_list):
	from datetime import datetime
	from erpnext.stock.get_item_details import get_item_details


	args = {
		"item_code":item_code ,              
		"price_list_currency": "INR",          
		"selling_price_list": price_list,  
		"conversion_rate": 1.0,                
		"doctype": "Sales Order",              
		 "transaction_date": datetime.today().strftime('%Y-%m-%d'),
		"company":frappe.defaults.get_user_default("Company"),
		"customer":"test",
	}

   
	if not item_code or not price_list:
		frappe.throw("Item code and price list are required.")

	price_data = get_item_details(args)
	frappe.errprint(price_data)

	if price_data:
		return price_data.price_list_rate
	else:
		frappe.msgprint(f"Price not found for item {item_code} in price list {price_list}.")
