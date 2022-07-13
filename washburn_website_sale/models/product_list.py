# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductList(models.Model):
    _name = 'product.list'
    _description = 'Product List'

    name = fields.Char(string='Name')
    product_ids = fields.Many2many('product.template', string='Products')
    partner_ids = fields.One2many('res.partner', inverse_name='product_list_id', string='Customers')
