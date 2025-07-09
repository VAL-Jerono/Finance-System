import frappe
from frappe.model.document import Document

def execute():
    if frappe.db.exists("DocType", "Imprest Request"):
        print("DocType 'Imprest Request' already exists. Skipping creation.")
        return

    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Imprest Request",
        "module": "Finance",
        "custom": 1,
        "fields": [
            {"fieldname":"requester","label":"Requester","fieldtype":"Link","options":"Employee"},
            {"fieldname":"department","label":"Department","fieldtype":"Link","options":"Department"},
            {"fieldname":"request_date","label":"Request Date","fieldtype":"Date"},
            {"fieldname":"purpose","label":"Purpose","fieldtype":"Small Text"},
            {"fieldname":"requested_amount","label":"Requested Amount","fieldtype":"Currency"},
            {"fieldname":"cost_center","label":"Project / Cost Center","fieldtype":"Link","options":"Cost Center"},
            {"fieldname":"expected_liquidation_date","label":"Expected Liquidation Date","fieldtype":"Date"},
            {"fieldname":"status","label":"Status","fieldtype":"Select","options":"Draft\nRequested\nApproved\nRejected\nDisbursed"},
            {"fieldname":"linked_payment_entry","label":"Linked Payment Entry","fieldtype":"Link","options":"Fin Payment Entry"},
            {"fieldname":"remarks","label":"Remarks","fieldtype":"Small Text"}
        ],
        "is_submittable": 1,
        "permissions": [
            {
                "role": "System Manager",
                "read": 1,
                "write": 1,
                "create": 1,
                "submit": 1,
                "cancel": 1
            }
        ]
    })
    doc.insert()
    frappe.db.commit()
    print("✅ Created custom DocType: Imprest Request")
