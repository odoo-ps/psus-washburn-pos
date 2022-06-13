from odoo import _, api, fields, models
from odoo.http import request

class StockProductionLot(models.Model):
    _inherit = "stock.production.lot"

    boxed_tracking_number = fields.Char(string="Boxed tracking number")
    customer_part_number = fields.Char(string="Customer part number")
    incident_number = fields.Char(string="Incident number")
    store_number = fields.Char(string="Store number")

    condition_id = fields.Many2one('stock.production.lot.condition', string="Condition")
    partner_id = fields.Many2one('res.partner', string="Owner")
    sale_order_id = fields.Many2one('sale.order', string="Sale order")
    current_location_id = fields.Many2one('stock.location', compute='_compute_current_location_id')

    def _compute_current_location_id(self):
        for record in self:
            record.current_location_id = record.quant_ids.filtered(lambda quant: quant.quantity > 0)[:1].location_id

    def _product_status_get_portal_domain(self):
        if self.env.user.has_group('stock.group_stock_user'):
            return []

        return [('partner_id.id', '=', request.env.user.partner_id.id)]
