# -*- coding: utf-8 -*-
{
    "name": "motorcycle_stock",
    "summary": """
        Module to add motorcycle_registry information to the product template.
    """,
    "description": """
        Adds a new product type called 'Motorcycle' which contains additional fields specific to their motorcycle models.
    """,
    "author": "elct-odoo",
    "website": "www.odoo.com",
    "license": "OPL-1",
    "category": "Kawiil/",
    "version": "0.1",
    "depends": ["motorcycle_registry", "product"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_inherit.xml",
    ],
}
