# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import _, api, fields, models
from odoo.exceptions import UserError

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    display_name = fields.Char(compute='_compute_display_name', store=True)
    
class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    print_format = fields.Selection(selection_add=[
        ('3x7x32*25', '3x7 (32mmx25mm)' )
        ], ondelete={'3x7x32*25': lambda recs: recs.write({'print_format': '2x7xprice'})})


    def _prepare_report_data(self):
        xml_id, data = super(ProductLabelLayout, self)._prepare_report_data()

        if self.move_line_ids:
            data['abbr'] = self.move_line_ids[0].picking_id.partner_id.abbreviation

        return xml_id, data