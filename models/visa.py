from odoo import models, fields, api


class Visa(models.Model):
    _name = 'housemaid.visa'
    _description = 'Full Housemaid Visa Transaction Information'

    name = fields.Many2one(comodel_name='housemaid.application', string='name', domain=[('state', '=', 'reservation')])
    customer = fields.Char(string="Customer", required=False, size=120, )
    visa_number = fields.Char(string="Visa Number", required=False, size=80, )
    labor_id = fields.Char(string="Labor ID", required=False, size=80, )
    visa_create_date = fields.Date(string="Visa Create Date", required=False, )
    visa_receive_date = fields.Date(string="Visa Receive Date", required=False, defualt=fields.Date.context_today, )
    visa_sent_date = fields.Date(string="Visa Sent Date", required=False, )
    cash_payment_amount = fields.Integer(string="Cash Payment", default=0, required=True, copy=True)
    knet_payment_amount = fields.Integer(string="KNET Payment", default=0, required=True, copy=True)
    vise_payment_amount = fields.Integer(string="VISA Payment", default=0, required=True, copy=True)
    other_payment_amount = fields.Integer(string="Other Payment", default=0, required=True, copy=True)
    other_payment_method = fields.Selection(selection=[('american_express', 'American Express'),
                                                       ('masterCard', 'MasterCard'),
                                                       ('western_union', 'Western Union'),
                                                       ('paypal', 'PayPal'),
                                                       ('buckaroo', 'Buckaroo'),
                                                       ('payu_latam', 'PayU Latam'),
                                                       ('payumoney', 'PayUmoney'), ],
                                            string="Other Payment Method",
                                            required=False, )
    remarks = fields.Char(string="Remarks", required=False, size=255, )
    status = fields.Selection(string="Visa Status", required=True,
                              selection=[('active', 'Active Visa'),
                                         ('canceled', 'Canceled Visa'), ], default='active')
