import frappe

def on_submit(doc, method):
    if doc.references:
        for ref in doc.references:
            if ref.reference_doctype == "Imprest Request":
                frappe.db.set_value("Imprest Request", ref.reference_name, "linked_payment_entry", doc.name)
                frappe.db.commit()
                print(f"✅ Linked {doc.name} to Imprest Request {ref.reference_name}")
