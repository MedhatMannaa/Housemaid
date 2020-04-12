from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError

logger = logging.getLogger(__name__)


class ExpectingArrival(models.Model):
    _name = 'housemaid.expectingarrival'
    _description = 'Full Housemaid Expecting Arrival Transaction Details'

    name = fields.Many2one(comodel_name='housemaid.application', string='name', domain=[('state', '=', 'visa')])
    email_date = fields.Date(string="Email Date", required=False, )
    expect_arrival_date = fields.Datetime(string="Expecting Arrival Date", required=False, )
    remarks = fields.Char(string="Remarks", required=False, size=255, )
    state = fields.Selection(string="Visa Status", required=True,
                              selection=[('active', 'Active Expect Arrival'),
                                         ('havevisa', 'Active Expect Arrival'),
                                         ('canceled', 'Canceled Visa'), ], default='active')
    # override create function
    @api.model
    def create(self, vals):
        try:

            expectingarrival = super(ExpectingArrival, self).create(vals)

            application = self.env['housemaid.application'].search([('id', '=', expectingarrival.name.id)], limit=1)
            application.state = 'expecting_arrival'

            return expectingarrival


        except Exception as e:
            logger.exception("Create Method")
            raise ValidationError(e)

    # override write function
    def write(self, vals):
        try:

            expectingarrival = super(ExpectingArrival, self).write(vals)
            return expectingarrival


        except Exception as e:
            logger.exception("Write Method")
            raise ValidationError(e)

    # override unlink function
    def unlink(self):
        try:

            expectingarrival = super(ExpectingArrival, self).unlink()
            return expectingarrival


        except Exception as e:
            logger.exception("Unlink Method")
            raise ValidationError(e)

