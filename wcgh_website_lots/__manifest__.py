{
    "name": "WCGH Website Lots",
    "summary": """Display 'stock.product.lot' in /my portal""",
    "category": "",
    "version": "15.0.1.0.0",
    "author": "Odoo PS",
    "website": "https://www.odoo.com",
    "license": "OEEL-1",
    "depends": [
        'stock',
        'sale',
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/stock_production_lot.xml",
        "views/stock_production_lot_portal_templates.xml",
    ],
    "odoo_task_ids": [2875047],
}
