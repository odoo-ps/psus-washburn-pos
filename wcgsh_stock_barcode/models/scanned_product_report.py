# -*- coding: utf-8 -*-
from odoo import api, models

import logging

_logger = logging.getLogger(__name__)

class ProductLabelWCGSHReport(models.AbstractModel):
    _name = 'report.wcgsh_stock_barcode.report_scanned_product_barcode'

    def _get_report_values(self, docids, data=None):
        product_id = data.get('product_id')
        owner_id = data.get('owner_id')
        barcode = data.get('barcode')
        products = self.env['product.product'].browse([product_id])
        abbr = self.env['res.partner'].browse([owner_id]).abbreviation
        return {
            'barcode': barcode,
            'abbr': abbr,
            'docids': docids,
            'docs': products,
        }