from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_open_summary_wizard(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Resumen del Pedido',
            'res_model': 'sale.summary.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_order_id': self.id,
            },
        }