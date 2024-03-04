# -*- coding: utf-8 -*-
{
    "name": "motorcycle_website",
    "summary": """
        Adds compare page for motorcycle models""",
    "description": """
        Adds a compare page where you will see all the different 
        Motorcycle Models with their specs to compare each model's 
        features and power easily.
    """,
    "license": "OPL-1",
    "author": "elct-odoo",
    "website": "",
    "category": "Kawiil/",
    "version": "0.1",
    "depends": ["motorcycle_registry", "motorcycle_stock", "website"],
    "data": [
        "views/motorcycle_registry_web_templates.xml",
    ],
}
