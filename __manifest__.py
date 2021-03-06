# -*- coding: utf-8 -*-
{
    'name': "housemaid",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Housemaid System 
    """,

    'author': "Medhat Mannaa",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/housemaid_security.xml',
        'security/ir.model.access.csv',
        'views/application_view.xml',
        'views/reservation_view.xml',
        'views/visa_view.xml',
        'views/expecting_arrival_view.xml',
        'views/arrived_housemaid_view.xml',
        'views/deliverd_housemaid_view.xml',
        'views/external_offices_view.xml',
        'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/exernal_offices_demo.xml',
        'demo/applications_demo.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
