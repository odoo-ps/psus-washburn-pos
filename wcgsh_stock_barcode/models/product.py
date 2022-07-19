# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models

class ProductLabelLayout(models.Model):
    _inherit = 'product.product'

    display_name = fields.Char('Display Name', compute="_compute_display_name", store=True)
    
    def action_scan_print(self, product_id, barcode=False, owner_id=False, pickingId=False):
        data = {'product_id': int(product_id), 'barcode': barcode, 'owner_id': int(owner_id)}
        result = False
        if pickingId:
            picking = self.env['stock.picking'].browse([pickingId])
            if len(picking.ids) > 0 and picking.picking_type_id.code == 'incoming':
                result = self.env.ref('wcgsh_stock_barcode.report_scanned_barcodes').report_action(None, data=data)
        return result