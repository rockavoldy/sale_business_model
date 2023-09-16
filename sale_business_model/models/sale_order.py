from odoo import models, fields

BUSINESS_MODEL = [
    ('retail', 'Retail'),
    ('corporate', 'Corporate'),
    ('subscription', 'Subscription')
]

BUSINESS_MODEL_SHORTCODE = {
    'retail':'RT',
    'corporate':'CORP',
    'subscription':'SUB'
}

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    business_model = fields.Selection(BUSINESS_MODEL, string='Business Model', default='retail')
    
    def name_get(self):
        """ Override display_name to add business_model short name if business model is set """
        if not self.business_model:
            return super(SaleOrder, self).name_get()
        
        res = []
        for order in self:
            name = order.name
            if order.business_model:
                name = '[%s] - %s' % (BUSINESS_MODEL_SHORTCODE[order.business_model], order.name)
            res.append((order.id, name))
        return res

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    order_business_model = fields.Selection(related='order_id.business_model')