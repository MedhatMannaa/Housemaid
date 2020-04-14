from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError

logger = logging.getLogger(__name__)


class DeliverdHousemaid(models.Model):
    _name = 'housemaid.deliverdhousemaid'
    _description = 'Full Housemaid Visa Transaction Information'

    name = fields.Many2one(comodel_name='housemaid.application', string='name', domain=[('state', '=', 'arrived')])
    create_date = fields.Date(string="Deliver Date", required=False, )
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
    state = fields.Selection(string="Deliver Housemaid Status", required=True,
                              selection=[('active', 'Housemaid Deliverd'),
                                         ('canceled', 'Deliverd Canceled'), ], default='active')
    # override create function
    @api.model
    def create(self, vals):
        try:

            deliverdhousemaid = super(DeliverdHousemaid, self).create(vals)

            application = self.env['housemaid.application'].search([('id', '=', deliverdhousemaid.name.id)], limit=1)
            application.state = 'delivered'

            return deliverdhousemaid


        except Exception as e:
            logger.exception("Create Method")
            raise ValidationError(e)

    # override write function
    def write(self, vals):
        try:

            deliverdhousemaid = super(DeliverdHousemaid, self).write(vals)
            return deliverdhousemaid


        except Exception as e:
            logger.exception("Write Method")
            raise ValidationError(e)

    # override unlink function
    def unlink(self):
        try:

            deliverdhousemaid = super(DeliverdHousemaid, self).unlink()
            return deliverdhousemaid


        except Exception as e:
            logger.exception("Unlink Method")
            raise ValidationError(e)

