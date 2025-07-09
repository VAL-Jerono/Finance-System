import frappe

def execute():
    if not frappe.db.exists("Custom Field", "Imprest Request-status"):
        field = frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Imprest Request",
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "insert_after": "imprest_request_type",  # Change if needed
            "options": "Draft\nRequested\nApproved\nRejected\nDisbursed",
            "default": "Draft"
        })
        field.insert()
        frappe.db.commit()
        print("✅ 'status' field added to Imprest Request.")
    else:
        print("✅ 'status' field already exists.")
