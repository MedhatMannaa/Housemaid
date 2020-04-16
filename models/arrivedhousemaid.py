from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError

logger = logging.getLogger(__name__)


class ArrivedHousemaid(models.Model):
    _name = 'housemaid.arrivedhousemaid'
    _description = 'Full Housemaid Arrived Transaction'

    name = fields.Many2one(comodel_name='housemaid.application', string='name',
                           domain=[('state', '=', 'expecting_arrival')])
    driver_name = fields.Char(string="Receiver Employee", required=False, size=120, )
    arrival_date = fields.Datetime(string="Arrival Date&time", required=False, )
    remarks = fields.Char(string="Remarks", required=False, size=255, )
    state = fields.Selection(string="Arrived Status", required=True,
                             selection=[('active', 'Arrived'),
                                        ('canceled', 'Canceled Delivered'), ], default='active')

    # override create function
    @api.model
    def create(self, vals):
        try:

            arrivedhousemaid = super(ArrivedHousemaid, self).create(vals)

            application = self.env['housemaid.application'].search([('id', '=', arrivedhousemaid.name.id)], limit=1)
            application.state = 'arrived'

            return arrivedhousemaid


        except Exception as e:
            logger.exception("Create Method")
            raise ValidationError(e)

    # override write function
    def write(self, vals):
        try:

            arrivedhousemaid = super(ArrivedHousemaid, self).write(vals)
            return arrivedhousemaid


        except Exception as e:
            logger.exception("Write Method")
            raise ValidationError(e)

    # override unlink function
    def unlink(self):
        try:

            arrivedhousemaid = super(ArrivedHousemaid, self).unlink()
            return arrivedhousemaid


        except Exception as e:
            logger.exception("Unlink Method")
            raise ValidationError(e)

    def arrivedhousemaid_cancel_action(self):
        arrived = self.env['housemaid.arrivedhousemaid'].search([('name', '=', self.name.id)], limit=1)
        if not arrived:
            self.state = 'canceled'
            application = self.env['housemaid.application'].search([('id', '=', self.name.id)], limit=1)
            application.state = 'visa'
        else:
            raise ValidationError("There is Expecting Arrival Transaction for This Application")