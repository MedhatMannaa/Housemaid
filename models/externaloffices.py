from odoo import models, fields, api


class ExternalOffices(models.Model):
    _name = 'housemaid.externaloffices'
    _description = 'Full External Offices Information'

    name = fields.Char(string="Office Name",  size=100, )
    office_short_ref = fields.Char(string="Office Short Ref",  size=60, )
    office_logo = fields.Image(string="Office Licence", )
    owner_name = fields.Char(string="Office Owner Name",  size=120, )
    country = fields.Many2one(comodel_name='res.country', string='Nationality')
    adress = fields.Char(string="Address Details",  size=60, )
    bank_name = fields.Many2one('res.partner.bank', string="Bank Name", ondelete='restrict', copy=False, )
    email = fields.Char(string="Email Address",  size=100, )
    phone_number = fields.Char(string="Contact Number",  size=60, )
    fax_number = fields.Char(string="FAX Number",  size=60, )
    currency = fields.Many2one(comodel_name='res.currency', string='Currency')