from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError

logger = logging.getLogger(__name__)


class ExpectingArrival(models.Model):
    _name = 'housemaid.expectarrival'
    _description = 'Full Housemaid Visa Transaction Information'

    name = fields.Many2one(comodel_name='housemaid.application', string='name', domain=[('state', '=', 'visa')])
    email_receive_date = fields.Date(string="Email Receive Date", required=False, defualt=fields.Date.context_today, )
    expecting_arrival_date = fields.Datetime(string="Expecting Arrival Date", required=True, )
    remarks = fields.Char(string="Remarks", required=False, size=255, )
    state = fields.Selection(string="Visa Status", required=True,
                              selection=[('active', 'Active Expecting Date'),
                                         ('canceled', 'Canceled Active Expecting'), ], default='active')
    # override create function
    @api.model
    def create(self, vals):
        try:

            expectarrival = super(ExpectingArrival, self).create(vals)

            application = self.env['housemaid.application'].search([('id', '=', expectarrival.name.id)], limit=1)
            application.state = 'expecting_arrival'

            return expectarrival


        except Exception as e:
            logger.exception("Create Method")
            raise ValidationError(e)

    # override write function
    def write(self, vals):
        try:

            expectarrival = super(ExpectingArrival, self).write(vals)
            return expectarrival


        except Exception as e:
            logger.exception("Write Method")
            raise ValidationError(e)

    # override unlink function
    def unlink(self):
        try:

            expectarrival = super(ExpectingArrival, self).unlink()
            return expectarrival


        except Exception as e:
            logger.exception("Unlink Method")
            raise ValidationError(e)

