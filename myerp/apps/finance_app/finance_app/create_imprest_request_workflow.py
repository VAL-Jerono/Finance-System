import frappe

def execute():
    if frappe.db.exists("Workflow", "Imprest Request Approval"):
        print("Workflow already exists.")
        return

    workflow = frappe.get_doc({
        "doctype": "Workflow",
        "workflow_name": "Imprest Request Approval",
        "document_type": "Imprest Request",
        "is_active": 1,
        "send_email_alert": 1,
        "update_field": "status",
        "states": [
            {
                "state": "Draft",
                "doc_status": 0,
                "allow_edit": "Employee"
            },
            {
                "state": "Requested",
                "doc_status": 0,
                "allow_edit": "Finance Manager"
            },
            {
                "state": "Disbursed",
                "doc_status": 1,
                "allow_edit": "Cashier"
            }
        ],
        "transitions": [
            {
                "state": "Draft",
                "action": "Submit Request",
                "next_state": "Requested",
                "allowed": "Employee"
            },
            {
                "state": "Requested",
                "action": "Disburse",
                "next_state": "Disbursed",
                "allowed": "Cashier"
            }
        ]
    })

    workflow.insert(ignore_permissions=True)
    print("✅ Workflow created: Imprest Request Approval")
