import frappe
from frappe.utils import today, add_days

def execute():
    overdue_requests = frappe.db.get_all("Imprest Request", filters={
        "status": "Disbursed"
    }, fields=["name", "expected_liquidation_date", "requester"])

    for req in overdue_requests:
        if req.expected_liquidation_date and req.expected_liquidation_date < today():
            requester = frappe.get_doc("Employee", req.requester)
            user = frappe.db.get_value("User", {"email": requester.user_id}, "name")

            if user:
                frappe.sendmail(
                    recipients=[user],
                    subject="🔔 Liquidation Overdue",
                    message=f"Imprest Request <b>{req.name}</b> was disbursed but not liquidated by {req.expected_liquidation_date}. Kindly submit your liquidation.",
                )
    print("✅ Checked and alerted overdue liquidations.")
