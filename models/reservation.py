from odoo import models, fields, api


class reservation(models.Model):
    _name = 'housemaid.reservation'
    _description = 'Full Housemaid Reservation Transaction Information'

    application_id = fields.Many2one('housemaid.application', 'Housemaid')
    customer_name = fields.Char(string="Customer Name", required=True, size=80, )
    customer_area = fields.Char(string="Customer Area", required=True, size=80, )
    customer_phone = fields.Char(string="Customer Phone", required=True, size=80, )
    reservation_date = fields.Date(string="Reservation Date", required=True, defualt=fields.Date.context_today, )
    due_amount = fields.Integer(string="DUE Amount", required=True, copy=True)
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