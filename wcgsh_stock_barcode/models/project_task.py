# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import _, api, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    product_part = fields.Char(string='Product/Part', store=True)
    task_owner = fields.Char(string='Owner', store=True)