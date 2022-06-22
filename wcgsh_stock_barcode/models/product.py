# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import _, api, fields, models

class ProductLabelLayout(models.Model):
    _inherit = 'product.product'

    display_name = fields.Char('Display Name', compute="_compute_display_name", store=True)