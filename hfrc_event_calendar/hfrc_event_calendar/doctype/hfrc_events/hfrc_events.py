# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt


import frappe
import json
from frappe import _
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

class HFRCEvents(WebsiteGenerator):
	pass

@frappe.whitelist()
def get_events(start, end, user=None, filters=None):
	if not user:
		user = frappe.session.user


	tables = ["`tabHFRC Events`"]
	
	events = frappe.db.sql("""
		SELECT `tabHFRC Events`.name,
				`tabHFRC Events`.event_title,				
				`tabHFRC Events`.start_date,
				`tabHFRC Events`.end_date			
		FROM {tables}
		ORDER BY `tabHFRC Events`.start_date""".format(
			tables=", ".join(tables)
		), {
			"start": start,
			"end": end
		}, as_dict=1)

	return events	
	
