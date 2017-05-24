# -*- coding: utf-8 -*-
{
    'name': "Open Academy Level",

    'summary': """Manage trainings for levels""",

    'description': """
        Open Academy level extension module for managing trainings:
            - training courses for levels
            - training sessions
            - attendees registration
    """,

    'author': "Felipe Peiro",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','openacademy'],

    # always loaded
    'data': [
        'views/openacademy.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
    'installable': True,
    'active': False,
}
