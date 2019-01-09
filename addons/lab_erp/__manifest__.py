# -*- coding: utf-8 -*-
{
    'name': "lab_erp",

    'summary': """
        Website C2C sales books""",

    'description': """
        Allow merchants sale our book in website.
    """,

    'author': "Peter Dinh",
    'website': "http://www.peterdinh.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
        # 'views/login_signup_templates.xml',
        # 'data/mail_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}