# -*- coding: utf-8 -*-
{
    "name": "motorcycle_map",
    "summary": """
        Adds a map to the motorcycle model""",
    "description": """
        Adds ability to see on a map the location of their registered motorcycles
    """,
    "license": "OPL-1",
    "author": "elct-odoo",
    "website": "https://www.odoo.com",
    "category": "Kawiil/",
    "version": "0.1",
    "depends": ["motorcycle_registry", "web_map"],
    "data": [
        "views/motorcycle_registry_map_view.xml",
    ],
}
