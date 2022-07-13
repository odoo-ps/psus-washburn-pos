# -*- coding: utf-8 -*-

{
    'name': 'Product List per Customer on Ecommerce',
    'summary': 'Product List per Customer on Ecommerce',
    'sequence': 100,
    'license': 'OPL-1',
    'website': 'https://www.odoo.com',
    'version': '1.1',
    'author': 'Odoo Inc',
    'description': """
        Task ID: 2879021
        - Add a product list, that associates customers with which products they can buy
        - Add filter for products on the website
    """,
    'category': 'Custom Development',

    # any module necessary for this one to work correctly
    'depends': ['website_sale', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_list_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
