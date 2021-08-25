frappe.views.calendar["HFRC Events"] = {
	field_map: {
		"start": "start_date",
		"end": "end_date",
		"id": "event_title",
		//"allDay": "all_day",
		"title": "event_title",
		//"status": "event_type",
		//"color": "color"
	},
	style_map: {
		"Public": "success",
		"Private": "info"
	},
	get_events_method: "hfrc_event_calendar.hfrc_event_calendar.doctype.hfrc_events.hfrc_events.get_events"
    
}