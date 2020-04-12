from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError

logger = logging.getLogger(__name__)


class Reservation(models.Model):
    _name = 'housemaid.reservation'
    _description = 'Full Housemaid Reservation Transaction Information'

    name = fields.Many2one(comodel_name='housemaid.application', string='name',
                           domain=[('state', '=', 'new_application')], )
    reservation_date = fields.Date(string="Reservation Date", required=False, defualt=fields.Date.context_today, )
    customer_name = fields.Char(string="Customer Name", required=False, size=80, )
    customer_area = fields.Char(string="Customer Area", required=False, size=80, )
    customer_phone = fields.Char(string="Customer Phone", required=False, size=80, )
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
    state = fields.Selection(string="Reservation Status", required=False,
                             selection=[('active', 'Active Reservation'),
                                        ('canceled', 'Canceled Reservation'), ], default='active')

    # override create function
    @api.model
    def create(self, vals):
        try:

            reservation = super(Reservation, self).create(vals)

            application = self.env['housemaid.application'].search([('id', '=', reservation.name.id)], limit=1)
            application.state = 'reservation'

            return reservation


        except Exception as e:
            logger.exception("Create Method")
            raise ValidationError(e)

    # override write function
    def write(self, vals):
        try:

            reservation = super(Reservation, self).write(vals)
            return reservation


        except Exception as e:
            logger.exception("Write Method")
            raise ValidationError(e)

    # override unlink function
    def unlink(self):
        try:

            reservation = super(Reservation, self).unlink()
            return reservation


        except Exception as e:
            logger.exception("Unlink Method")
            raise ValidationError(e)

    def reservatioin_cancelreservation_byemployer_action(self):
        visa = self.env['housemaid.visa'].search([('name', '=', self.name.id)], limit=1)
        if not visa:
            self.state = 'canceled'
            application = self.env['housemaid.application'].search([('id', '=', self.name.id)], limit=1)
            application.state = 'new_application'
        else:
            raise ValidationError("There is Visa for This Application")

    def reservatioin_cancelreservation_byexofice_action(self):
        visa = self.env['housemaid.visa'].search([('name', '=', self.name.id)], limit=1)
        if not visa:
            self.state = 'canceled'
            application = self.env['housemaid.application'].search([('id', '=', self.name.id)], limit=1)
            application.state = 'cancel_application'
        else:
            raise ValidationError("There is Visa for This Application")
