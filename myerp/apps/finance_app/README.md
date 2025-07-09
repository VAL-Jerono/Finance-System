

````markdown
# Finance App

A modular and scalable finance system built from scratch using the **Frappe Framework** and **ERPNext**.  
This app is designed to streamline and digitize **core financial operations** for businesses, institutions, or public sector agencies.

---

## ✅ Features Implemented

- **Custom Frappe App**: `finance_app` created and structured following Frappe best practices.
- **Custom DocTypes**:

  | DocType                   | Function |
  |---------------------------|----------|
  | **Budget Plan**           | Define and allocate budgets by department, account, and fiscal year to ensure proper financial planning and control. |
  | **Imprest Request**       | Allow employees to request advance funds for operational needs such as travel or project expenses, with built-in approval workflows. |
  | **Imprest Liquidation**   | Submit receipts and justifications to account for previously disbursed funds, closing the loop on imprest processes. |
  | **Fin Payment Entry**     | Custom payment tracking entry linked to imprest disbursements or invoice clearances, ensuring traceability. |
  | **Invoice (Customized)**  | Tailored for internal payment workflows with enhanced field mappings and linkage to budget items. |
  | **Invoice Item (Customized)** | Includes extended fields for improved item tracking and budget association. |
  | **Expense Claim (Customized)** | Integrated with imprest workflows to improve accountability on reimbursable employee expenses. |

---

- **Exported Fixtures**:
  - All custom fields and DocTypes exported as version-controlled JSON for deployment across environments.
- **Hooks Configuration**:
  - Automatically loads fixtures during installation for consistent setup.
- **Workflows**:
  - Approval workflows implemented for Imprest Requests and Liquidations.
  - Roles: Employee, Finance Manager, Cashier.
- **Automation Scripts**:
  - Scripts to auto-link payment entries.
  - Email alerts for overdue liquidations.
  - Status updates handled via patch scripts.

---

## 🧪 How to Test

> Requirements: Frappe v14, ERPNext v14, Redis, Python 3.10+, Node.js 16+

### 1. Clone the Repo

```bash
git clone https://github.com/VAL-Jerono/Finance-System.git
cd Finance-System/myerp
````

### 2. Set Up Environment

```bash
python3 -m venv frappe-env
source frappe-env/bin/activate
```

### 3. Start Bench

```bash
bench start
```

Then visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🖼️ Previews

| Bench Start                                              | Budget Plan                                              | DocType                                           |
| -------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------- |
| ![Bench start](finance_app/public/images/benchstart.png) | ![Budget Plan](finance_app/public/images/budgetplan.png) | ![DocType](finance_app/public/images/doctype.png) |

---

## 🗂️ Folder Structure

```
finance_app/
├── finance_app/
│   ├── fixtures/                      # Exported DocTypes and fields
│   ├── config/                        # App configuration
│   ├── public/                        # Static files (images, JS, etc.)
│   │   └── images/                    # App screenshots
│   ├── templates/                     # Jinja templates
│   ├── hooks.py                       # Frappe app hooks
│   ├── patches.txt                    # Patch tracker
│   ├── create_imprest_request.py
│   ├── create_imprest_request_workflow.py
│   ├── create_imprest_liquidation.py
│   ├── create_imprest_liquidation_workflow.py
│   ├── payment_entry_auto_link.py
│   ├── email_alert_overdue_liquidation.py
│   └── ...
├── modules.txt
├── pyproject.toml
└── README.md
```

---

## 🔄 Workflows & Roles

* **Roles Defined**:

  * `Employee`: Initiates requests and submits liquidations.
  * `Finance Manager`: Reviews and approves requests.
  * `Cashier`: Disburses funds and updates statuses.

* **Workflow States**:

  * `Draft` → `Requested` → `Approved` → `Disbursed`

* **Workflow Actions**:

  * `Submit Request`, `Approve`, `Reject`, `Disburse`

---

## 📩 Notifications

* Automated **email alerts** sent for overdue imprest liquidations.
* Linked updates across `Imprest Request`, `Liquidation`, and `Fin Payment Entry` via scripts.

---

## 🔖 License

[MIT](./license.txt)

---

## 👤 Author

**VAL-Jerono**
GitHub: [VAL-Jerono](https://github.com/VAL-Jerono)

