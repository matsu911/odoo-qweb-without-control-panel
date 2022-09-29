# -*- coding: utf-8 -*-
{
    'name': "QWeb without ControlPanel",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "matsu911",
    'website': "https://github.com/matsu911/odoo-qweb-without-control-panel",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo-qweb-without-control-panel/static/src/js/QWebWithoutControlPanel.js',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'license': "AGPL-3",
    'installable': True,
}
