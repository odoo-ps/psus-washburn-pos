# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import _, api, fields, models


class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    print_format = fields.Selection(selection_add=[
        ('3x7x32*25', '3x7 (32mmx25mm)' )
        ], ondelete={'3x7x32*25': lambda recs: recs.write({'print_format': '2x7xprice'})})