# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Ncontract(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		
		from frappe.types import DF

		amended_from: DF.Link | None
		camera_accuracy: DF.Data
		commercial_activity: DF.Data
		commercial_record: DF.Data
		company_name: DF.Link
		contract_end_date: DF.Date
		contract_renew_type: DF.Literal["\u0644\u0627 \u064a\u062c\u062f\u062f", "\u064a\u062c\u062f\u062f"]
		contract_start_date: DF.Date
		contract_type: DF.Literal["\u0639\u0642\u062f \u0635\u064a\u0627\u0646\u0629 \u0633\u0646\u0648\u064a \u0645\u0642\u0627\u0628\u0644 \u0623\u062c\u0631", "\u0639\u0642\u062f \u0635\u064a\u0627\u0646\u0629 \u0633\u0646\u0648\u064a \u0645\u062c\u0627\u0646\u064a"]
		contract_value_with_tax: DF.Int
		customer_name: DF.Link | None
		disks_storage: DF.Data
		elevator_camera: DF.Data
		in_camera: DF.Data
		naming_series: DF.Literal["QN-.YYYY.-", "QN-.2023.-"]
		number_of_visits: DF.Literal["6"]
		out_camera: DF.Data
		recording_machine: DF.Data
		security_license: DF.Data
		slug_customer_name: DF.Data
		solid_disks: DF.Data
		storage_days: DF.Data
	# end: auto-generated types
	pass
