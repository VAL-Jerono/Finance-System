import frappe

def execute():
    if frappe.db.exists("DocType", "Imprest Liquidation"):
        print("✅ DocType 'Imprest Liquidation' already exists.")
        return

    doc = frappe.get_doc({
        "doctype": "DocType",
        "name": "Imprest Liquidation",
        "module": "Finance",
        "custom": 1,
        "fields": [
            {"fieldname":"imprest_request","label":"Imprest Request","fieldtype":"Link","options":"Imprest Request"},
            {"fieldname":"liquidation_date","label":"Liquidation Date","fieldtype":"Date"},
            {"fieldname":"expense_description","label":"Expense Description","fieldtype":"Small Text"},
            {"fieldname":"expense_category","label":"Expense Category","fieldtype":"Link","options":"Account"},
            {"fieldname":"amount_spent","label":"Amount Spent","fieldtype":"Currency"},
            {"fieldname":"amount_refunded","label":"Amount Refunded","fieldtype":"Currency"},
            {"fieldname":"supporting_documents","label":"Supporting Documents","fieldtype":"Attach"},
            {"fieldname":"remarks","label":"Remarks","fieldtype":"Small Text"},
            {"fieldname":"status","label":"Status","fieldtype":"Select","options":"Draft\nSubmitted\nApproved\nClosed"}
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
    print("✅ Created: Imprest Liquidation")
