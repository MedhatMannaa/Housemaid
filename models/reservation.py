from odoo import models, fields, api


class Reservation(models.Model):
    _name = 'housemaid.reservation'
    _description = 'Full Housemaid Reservation Transaction Information'

    name = fields.Many2one(comodel_name='housemaid.application', string='name', domain=[('state', '=', 'new_application')], )
    reservation_date = fields.Date(string="Reservation Date", required=True, defualt=fields.Date.context_today, )
    customer_name = fields.Char(string="Customer Name", required=True, size=80, )
    customer_area = fields.Char(string="Customer Area", required=True, size=80, )
    customer_phone = fields.Char(string="Customer Phone", required=True, size=80, )
    due_amount = fields.Integer(string="DUE Amount", required=True, copy=True)
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
    state = fields.Selection(string="Reservation Status", required=True,
                              selection=[('active', 'Active Reservation'),
                                         ('canceled', 'Canceled Reservation'), ], default=0)

    def reservatioin_cancelreservation_action(self):
        self.status = 'canceled'

    def reservatioin_reactivereservation_action(self):
        self.status = 'active'
