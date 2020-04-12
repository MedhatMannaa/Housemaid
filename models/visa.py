from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError

logger = logging.getLogger(__name__)


class Visa(models.Model):
    _name = 'housemaid.visa'
    _description = 'Full Housemaid Visa Transaction Information'

    name = fields.Many2one(comodel_name='housemaid.application', string='name', domain=[('state', '=', 'reservation')])
    visa_scan = fields.Image("Visa Scan", max_width=1920, max_height=1920)
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
    state = fields.Selection(string="Visa Status", required=True,
                              selection=[('active', 'Active Visa'),
                                         ('activewithvisa', 'Visa With Expecting Arrival'),
                                         ('canceled', 'Canceled Visa'), ], default='active')
    # override create function
    @api.model
    def create(self, vals):
        try:

            visa = super(Visa, self).create(vals)

            application = self.env['housemaid.application'].search([('id', '=', visa.name.id)], limit=1)
            application.state = 'visa'

            return visa


        except Exception as e:
            logger.exception("Create Method")
            raise ValidationError(e)

    # override write function
    def write(self, vals):
        try:

            visa = super(Visa, self).write(vals)
            return visa


        except Exception as e:
            logger.exception("Write Method")
            raise ValidationError(e)

    # override unlink function
    def unlink(self):
        try:

            visa = super(Visa, self).unlink()
            return visa


        except Exception as e:
            logger.exception("Unlink Method")
            raise ValidationError(e)

    def visa_cancelvisa_byemployer_action(self):
        expectingarrival = self.env['housemaid.visa'].search([('name', '=', self.name.id)], limit=1)
        if not expectingarrival:
            self.state = 'canceled'
            application = self.env['housemaid.application'].search([('id', '=', self.name.id)], limit=1)
            application.state = 'new_application'
        else:
            raise ValidationError("There is Expecting Arrival Transaction for This Application")

    def visa_cancelvisa_byexofice_action(self):
        expectingarrival = self.env['housemaid.visa'].search([('name', '=', self.name.id)], limit=1)
        if not expectingarrival:
            self.state = 'canceled'
            application = self.env['housemaid.application'].search([('id', '=', self.name.id)], limit=1)
            application.state = 'cancel_application'
        else:
            raise ValidationError("There is Expecting Arrival Transaction for This Application")
