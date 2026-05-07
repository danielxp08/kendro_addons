{
    'name': 'Kendro Hostfully Website',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Property management module with website carousel for Hostfully integration demo',
    'description': """
        Demo module for managing rental properties and displaying them on the website.
        Features:
        - Property model with images, price, location, bedrooms, bathrooms
        - Dynamic Carousel snippet integration for website
        - Demo data with 3 properties
    """,
    'author': 'Kendro Solutions',
    'website': 'https://kendrosolutions.com',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_views.xml',
        'views/backend_layout.xml',
    ],
    'demo': [
        'data/property_demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}