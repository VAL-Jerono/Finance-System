import frappe

def execute():
    if frappe.db.exists("Workflow", "Imprest Liquidation Approval Workflow"):
        print("✅ Workflow already exists.")
        return

    doc = frappe.get_doc({
        "doctype": "Workflow",
        "workflow_name": "Imprest Liquidation Approval Workflow",
        "document_type": "Imprest Liquidation",
        "is_active": 1,
        "send_email_alert": 1,
        "workflow_state_field": "status",
        "states": [
            {"state": "Draft", "doc_status": 0, "allow_edit": "Employee"},
            {"state": "Submitted", "doc_status": 0, "allow_edit": "Finance Manager"},
            {"state": "Approved", "doc_status": 0, "allow_edit": "Finance Manager"},
            {"state": "Closed", "doc_status": 1}
        ],
        "transitions": [
            {"state": "Draft", "action": "Submit", "next_state": "Submitted", "allowed": "Employee"},
            {"state": "Submitted", "action": "Approve", "next_state": "Approved", "allowed": "Finance Manager"},
            {"state": "Approved", "action": "Close", "next_state": "Closed", "allowed": "System Manager"}
        ]
    })
    doc.insert()
    frappe.db.commit()
    print("✅ Created Imprest Liquidation Workflow")
