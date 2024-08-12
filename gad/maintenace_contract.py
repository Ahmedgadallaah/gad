# Copyright (c) 2024, gad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MaintenaceContract(Document):
	pass

def companies_data(doc, method):

	customer = frappe.get_doc('Customer',  doc.customer_name)
	company  = frappe.get_doc('Company',   doc.company_name)
	doc.commercial_record=customer.commercial_record
	doc.commercial_activity=customer.commercial_activity
	doc.security_license=company.security_license
	
    