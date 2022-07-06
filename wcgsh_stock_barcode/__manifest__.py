# -*- coding: utf-8 -*-
{
    'name': "Washburn POS : Auto barcode printing",
    'summary': 'Auto print barcode labels',
    'sequence': 100,
    'license': 'OPL-1',
    'website': 'https://www.odoo.com',
    'version': '1.1',
    'author': 'Odoo Inc',
    'description': """
        Task id:  2830191
        'When we receive with the barcode scanner we would like to auto-print the serial number for each Stock Move line we receive.'
    """,
    'depends': ['stock_barcode', 'contacts', 'product', 'project'],
    'data': [
        'views/res_partner_views.xml',
        'views/product_product_templates.xml',
        'views/product_reports.xml',
        'views/project_task_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'wcgsh_stock_barcode/static/src/js/kanban_controller.js',
            'wcgsh_stock_barcode/static/src/js/barcode_picking_model.js',
            'wcgsh_stock_barcode/static/src/js/barcode_model.js',
        ],
        'web.report_assets_common': [
            'wcgsh_stock_barcode/static/src/scss/product_product_templates.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
