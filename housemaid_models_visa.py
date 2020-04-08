from odoo import models, fields, api


class visa(models.Model):
    _name = 'housemaid.visa'
    _description = 'Full Housemaid Visa Transaction Information'

    application_id = fields.Many2one('housemaid.application', 'Housemaid')
    visa_create_date = fields.Date(string="Visa Create Date", required=True, )
    visa_receive_date = fields.Date(string="Visa Receive Date", required=True, defualt=fields.Date.context_today, )
    visa_sent_date = fields.Date(string="Visa Sent Date", required=True, )
    cash_payment_amount = fields.Integer(string="Cash Payment", default='0.00', required=True, copy=True)
    knet_payment_amount = fields.Integer(string="KNET Payment", default='0.00', required=True, copy=True)
    vise_payment_amount = fields.Integer(string="VISA Payment", default='0.00', required=True, copy=True)
    other_payment_amount = fields.Integer(string="Other Payment", default='0.00', required=True, copy=True)
    other_payment_method = fields.Selection(selection=[('0', 'American Express'),
                                                       ('1', 'MasterCard'),
                                                       ('2', 'Western Union'),
                                                       ('3', 'PayPal'),
                                                       ('4', 'Buckaroo'),
                                                       ('5', 'PayU Latam'),
                                                       ('6', 'PayUmoney'), ],
                                            string="Other Payment Method",
                                            required=False, )
    remarks = fields.Char(string="Remarks", required=True, size=255, )