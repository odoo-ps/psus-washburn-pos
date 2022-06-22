# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models

class ProjectTask(models.Model):
    _inherit = 'project.task'

    product_part = fields.Char(string='Product/Part', store=True)
    owner = fields.Char(string='Owner', store=True)
    product_id = fields.Many2one('product.product',string='Product', compute='_compute_product_id', store=True)
    
    @api.depends('product_part')
    def _compute_product_id(self):
        for task in self:
            product = self.env['product.product'].search([('display_name','=',task.product_part)], limit=1)
            task.product_id = False
            if product:
                task.product_id = product
    
    def action_print_product_label(self, recordId):
        return self.env.ref('wcgsh_stock_barcode.report_project_task_barcodes').report_action(self.env["project.task"].browse([recordId]))