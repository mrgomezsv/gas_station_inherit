# -*- coding: utf-8 -*-
{
    'name': "nitro_custom1",

    'summary': """
        Agrega campos y grupos a la vista form, mas datos para control de ventas en general""",

    'description': """
        Agrega campos y grupos a la vista form, mas datos para control de ventas en general
    """,

    'author': "Treming",
    'website': "http://www.treming.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','nitro_gas'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
