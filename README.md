
# 📘 Finance System – Frappe/ERPNext Implementation

A modular and scalable finance system built from scratch using **Frappe Framework** and **ERPNext**, designed to streamline financial operations for businesses or public institutions.

---

##  Project Overview

This system is built to automate and integrate key financial workflows within an organisation. It ensures **transparency**, **accountability**, **auditability**, and **compliance** with internal and statutory regulations.

Modules implemented include:

1. Budgets & Budgetlines
2. Journals & Payroll Journal
3. General Ledger
4. Imprest Management
5. Trial Balance
6. Reconciliation
7. Payment Vouchers
8. Per Diem Management
9. Financial Reports

---

## System Architecture

### Framework:

* [Frappe](https://frappeframework.com/) – Backend & web framework (Python)
* [ERPNext](https://erpnext.com/) – Prebuilt modules and financial logic
* MariaDB – SQL-based database backend
* Redis – Background job queue
* NGINX – Web server
* Supervisor – Background process manager

---

## Module Descriptions

### 1. 📊 Budgets & Budgetlines

* **DocTypes:** Budget Plan, Budget Line Item
* **Features:**

  * Define annual/quarterly departmental budgets
  * Allocate funds to specific accounts or projects
  * Real-time budget utilisation reports

---

### 2. 🧾 Journals & Payroll Journal

* **DocTypes:** Journal Entry, Payroll Journal Entry
* **Features:**

  * Double-entry bookkeeping for income & expenses
  * Automatic payroll accounting integration
  * Tax and statutory compliance entries

---

### 3. 📘 General Ledger

* **DocTypes:** General Ledger Entry (built-in)
* **Features:**

  * Real-time, searchable ledger view
  * Automated population from journal entries
  * Drill-down capabilities to source documents

---

### 4. 💵 Imprest Management

* **DocTypes:** Imprest Request, Imprest Liquidation
* **Features:**

  * Request petty cash with approval routing
  * Expense reporting and liquidation tracking
  * Integration with payment vouchers

---

### 5. ⚖️ Trial Balance Management

* **Features:**

  * Real-time trial balance based on GL entries
  * Manual adjustment support
  * Integrated with reporting engine

---

### 6. 🔄 Reconciliation

* **DocTypes:** Bank Reconciliation Tool
* **Features:**

  * Match bank transactions with GL
  * Upload bank statements
  * Flag inconsistencies

---

### 7. 🧾 Payment Vouchers

* **DocTypes:** Payment Voucher
* **Features:**

  * Issue and track payments
  * Link to journal entries and approval workflows
  * Auto-generate GL entries

---

### 8. 🏕️ Per Diem Management

* **DocTypes:** Per Diem Policy, Per Diem Request
* **Features:**

  * Per diem calculator based on roles, location, and duration
  * Request approval workflow
  * Auto-liquidation integration

---

### 9. 📈 Reports

* **DocTypes:** Financial Report Templates
* **Features:**

  * Budget vs Actual
  * Trial Balance, P\&L, Cash Flow
  * Imprest Status, Payroll Summary
  * All downloadable to Excel/PDF

---

## ⚙️ Setup Instructions

```bash
# Step 1: Setup Frappe Environment
bench init finance-system --frappe-branch version-14
cd finance-system

# Step 2: Get ERPNext
bench get-app erpnext --branch version-14
bench new-site finance.local
bench --site finance.local install-app erpnext

# Step 3: (Optional) Add Custom App
bench new-app finance_custom
bench --site finance.local install-app finance_custom

# Step 4: Start Development Server
bench start
```

---

## 📅 Development Plan

| Week | Focus Area                | Milestone                          |
| ---- | ------------------------- | ---------------------------------- |
| 1    | Budgets & Journals        | DocTypes created, basic workflows  |
| 2    | Ledger & Payroll Journal  | Linked GL entries, payroll link    |
| 3    | Imprest & Vouchers        | Request + Liquidation flow         |
| 4    | Trial Balance & Reports   | Full trial balance & PDF reports   |
| 5    | Reconciliation & Per Diem | Upload tool + workflow             |
| 6    | Integration & QA          | Final testing, cleanup, deployment |

---

## 🔐 Roles & Permissions

| Role            | Permissions                               |
| --------------- | ----------------------------------------- |
| Finance Officer | Create/Edit Journals, Budgets, Imprest    |
| HR Manager      | View Payroll, Approve Per Diem            |
| Accountant      | GL, Trial Balance, Payment Vouchers       |
| Auditor         | Read-only access to all financial records |
| Admin           | Full access, system configuration         |

---

## 🛠️ Custom Scripts & Automation

* **Auto JV Creation:** Payment Voucher → Journal Entry
* **Alerts:** Overbudget alerts via email/SMS
* **Scheduled Jobs:** Monthly Trial Balance snapshot

---

## 🧪 Testing & Validation

All modules are tested using:

* Frappe's built-in **unit testing framework**
* Manual tests through custom forms
* Audit trail validation for all sensitive entries

---

## 📃 License

MIT License – Free to use, modify and extend.

---

## 💬 Contributors

Built by the Frappe community and contributors from the Finance System Working Group.

For feature requests, contact: \[[valerie.jerono)]

