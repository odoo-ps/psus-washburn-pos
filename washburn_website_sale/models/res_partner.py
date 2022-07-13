# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    product_list_id = fields.Many2one('product.list', string='Product List')
