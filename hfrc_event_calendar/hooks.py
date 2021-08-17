from . import __version__ as app_version

app_name = "hfrc_event_calendar"
app_title = "Hfrc Event Calendar"
app_publisher = "ppcrc"
app_description = "HFRC Event Calendar"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "nikhil.bk@jaansi.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hfrc_event_calendar/css/hfrc_event_calendar.css"
# app_include_js = "/assets/hfrc_event_calendar/js/hfrc_event_calendar.js"

# include js, css files in header of web template
# web_include_css = "/assets/hfrc_event_calendar/css/hfrc_event_calendar.css"
# web_include_js = "/assets/hfrc_event_calendar/js/hfrc_event_calendar.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hfrc_event_calendar/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

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
# 	"methods": "hfrc_event_calendar.utils.jinja_methods",
# 	"filters": "hfrc_event_calendar.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hfrc_event_calendar.install.before_install"
# after_install = "hfrc_event_calendar.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hfrc_event_calendar.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hfrc_event_calendar.tasks.all"
# 	],
# 	"daily": [
# 		"hfrc_event_calendar.tasks.daily"
# 	],
# 	"hourly": [
# 		"hfrc_event_calendar.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hfrc_event_calendar.tasks.weekly"
# 	],
# 	"monthly": [
# 		"hfrc_event_calendar.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "hfrc_event_calendar.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hfrc_event_calendar.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hfrc_event_calendar.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"hfrc_event_calendar.auth.validate"
# ]

