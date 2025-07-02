from odoo import models, fields

class SaleSummaryWizard(models.TransientModel):
    _name = 'sale.summary.wizard'
    _description = 'Resumen del Pedido de Venta'

    order_id = fields.Many2one('sale.order', string='Pedido de Venta', readonly=True)
    partner_id = fields.Many2one(related='order_id.partner_id', string='Cliente', readonly=True)
    amount_total = fields.Monetary(related='order_id.amount_total', string='Total', readonly=True)
    currency_id = fields.Many2one(related='order_id.currency_id', readonly=True)