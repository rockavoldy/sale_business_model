from odoo import models, fields

from .sale_order import BUSINESS_MODEL

class AccountTax(models.Model):
    _inherit = 'account.tax'

    business_model = fields.Selection(BUSINESS_MODEL, string='Business Model', default='retail')

