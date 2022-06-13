from odoo import _, api, fields, models


class StockProductionLotCondition(models.Model):
    _name = "stock.production.lot.condition"
    _description = "Stock production lot condition"

    name = fields.Char(string="Name")
