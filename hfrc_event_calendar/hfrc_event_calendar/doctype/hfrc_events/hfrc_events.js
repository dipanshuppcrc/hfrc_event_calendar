// Copyright (c) 2021, ppcrc and contributors
// For license information, please see license.txt

frappe.ui.form.on('HFRC Events', {
	category_type: function (frm) {
		let category = frm.doc.category_type

		frm.set_query('sub_category', () => {
			return {
				"filters": {
					"category": category
				}
			}
		})
	},
	location: function (frm) {
		frm.toggle_display('other_location', frm.doc.location === 'Other')
	}
});