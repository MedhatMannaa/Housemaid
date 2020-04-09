from odoo import models, fields, api


class externaloffices(models.Model):
    _name = 'housemaid.externaloffices'
    _description = 'Full External Offices Information'
    _rec_name = "office_name"

    office_name = fields.Char(string="Office Name", required=True, size=100, )
    office_short_ref = fields.Char(string="Office Short Ref", required=True, size=60, )
    office_logo = fields.Image(string="Office Licence", )
    owner_name = fields.Char(string="Office Owner Name", required=True, size=120, )
    country_id = fields.Many2one('res.country', 'Nationality')
    adress = fields.Char(string="Address Details", required=True, size=60, )
    bank_ac_number = fields.Char(string="Bank Account Number", required=True, size=60, )
    bank_name = fields.Char(string="Bank Name", required=True, size=150, )
    email = fields.Char(string="Email Address", required=True, size=100, )
    phone_number = fields.Char(string="Contact Number", required=True, size=60, )
    fax_number = fields.Char(string="FAX Number", required=True, size=60, )
    currency_id = fields.Many2one('res.currency', 'Currency')