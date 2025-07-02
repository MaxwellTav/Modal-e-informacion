{
    'name': 'primer módulo',
    'version': '18.0.0.0.0',
    'summary': 'Un módulo de ejemplo para probar y aprender',
    'description': 'Este es un módulo de ejemplo para demostrar la estructura básica de un módulo Odoo.',
    'author': 'Maxwell Tavares',
    'website': '',
    'category': 'Malware Tools',
    'depends': ['base', 'sale'],
    'data': [
        'views/sale_order_view_inherit.xml',
        'wizard/sale_summary_wizard_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}