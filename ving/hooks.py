app_name = "ving"
app_title = "Ving"
app_publisher = "GKT"
app_description = "GKT"
app_email = "ahmadsayyed66@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ving/css/ving.css"
# app_include_js = "/assets/ving/js/ving.js"

# include js, css files in header of web template
# web_include_css = "/assets/ving/css/ving.css"
# web_include_js = "/assets/ving/js/ving.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ving/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Task" : "custom_script/task/task.js",
    "Timesheet" : "custom_script/timesheet/timesheet.js",
    "Quotation" : "custom_script/quotation/quotation.js",
    "Stock Entry" : "custom_script/stock_entry/stock_entry.js"
}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ving/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "ving.utils.jinja_methods",
#	"filters": "ving.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ving.install.before_install"
# after_install = "ving.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ving.uninstall.before_uninstall"
# after_uninstall = "ving.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ving.utils.before_app_install"
# after_app_install = "ving.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ving.utils.before_app_uninstall"
# after_app_uninstall = "ving.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ving.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
"Task":"ving.custom_script.task.task.CustomTask",
"Quotation":"ving.custom_script.quotation.quotation.CustomQuotation",
    "Salary Slip": "ving.custom_script.salary_slip.salary_slip.CustomSalarySlip",

}





# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
  "ToDo":{
        "validate":"ving.custom_script.to_do.to_do.validate",
    },
    "Lead": {
        "after_insert": "ving.custom_script.lead_address.lead_address.create_lead_address",
    }
    "Stock Entry":{
        "on_submit":"ving.custom_script.stock_entry.stock_entry.on_submit",
        "on_cancel":"ving.custom_script.stock_entry.stock_entry.on_cancel",
    },
    "Payment Entry":{
        "on_submit":"ving.custom_script.payment_entry.payment_entry.on_submit",
        "on_cancel":"ving.custom_script.payment_entry.payment_entry.on_cancel",
    },
    # "Item Price":{
    #     "validate":"ving.custom_script.item_price_list.item_price_list.validate",
    #      "on_trash":"ving.custom_script.item_price_list.item_price_list.on_trash",
    # },
   
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"ving.tasks.all"
#	],
#	"daily": [
#		"ving.tasks.daily"
#	],
#	"hourly": [
#		"ving.tasks.hourly"
#	],
#	"weekly": [
#		"ving.tasks.weekly"
#	],
#	"monthly": [
#		"ving.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "ving.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "ving.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "ving.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ving.utils.before_request"]
# after_request = ["ving.utils.after_request"]

# Job Events
# ----------
# before_job = ["ving.utils.before_job"]
# after_job = ["ving.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ving.auth.validate"
# ]
