# -*- coding: utf-8 -*-
{
    "name": "Motorcycle Registry",
    "summary": """
        Track the Motorcycle Registration and Ownership of each motorcycle of the brand""",
    "description": """
        Custom development for Kawill Motorcycles, a motorcycle manufacturer based in Mexico City. This app aims to keep track of the Motorcycle Registration and Ownership of each motorcycle of the brand.
    """,
    "license": "OPL-1",
    "author": "elct-odoo",
    "website": "https://www.odoo.com",
    "category": "Kawiil/",
    "version": "0.1",
    "depends": ["base"],
    "data": [
        "views/views.xml",
        "views/templates.xml",
    ],
    "demo": [
        "demo/motorcycle_registry_demo.xml",
    ],
    "application": True,
}
