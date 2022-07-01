# -*- coding: utf-8 -*-

from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    def action_print_slip(self, recordId):
        result = self.env.ref('wcgsh_stock_barcode.report_receipt_barcodes').report_action(self.env["stock.picking"].browse([recordId]))
        return result