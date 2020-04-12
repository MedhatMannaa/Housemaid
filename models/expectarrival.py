from odoo import models, fields, api


class ExpectingArrival(models.Model):
    _name = 'housemaid.expectarrival'
    _description = 'Full Housemaid Expecting Arrival Transaction Information'

    name = fields.Many2one(comodel_name='housemaid.application', string='name', domain=[('state', '=', 'visa')])
    email_receive_date = fields.Date(string="Email Receive Date", required=False, defualt=fields.Date.context_today, )
    expecting_arrival_date = fields.Datetime(string="Expecting Arrival Date", required=True, )
    remarks = fields.Char(string="Remarks", required=False, size=255, )
    state = fields.Selection(string="Expecting Arrival Status", required=True,
                              selection=[('active', 'Active Expecting Date'),
                                         ('havevisa', 'Active Expecting Date With Visa'),
                                         ('canceled', 'Canceled Active Expecting'), ], default='active')
