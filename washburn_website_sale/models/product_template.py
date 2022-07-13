# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.osv import expression


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def _search_build_domain(self, domain_list, search, fields, extra=None):
        res = super(ProductTemplate, self)._search_build_domain(domain_list, search, fields, extra=extra)
        if self.env.user.partner_id.product_list_id:
            res = expression.AND([res, [('id', 'in', self.env.user.partner_id.product_list_id.product_ids.ids)]])
        return res





