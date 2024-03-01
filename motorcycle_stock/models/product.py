from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    battery_capacity = fields.Selection(
        selection=[
            ("xs", "Small"),
            ("0m", "Medium"),
            ("0l", "Large"),
            ("xl", "Extra Large"),
        ]
    )
    horsepower = fields.Float(string="Horsepower")
    top_speed = fields.Float(string="Top Speed")
    torque = fields.Float(string="Torque (Nm)")
    charge_time = fields.Float(string="Charge Time")
    range = fields.Float(string="Range")
    curb_weight = fields.Float(string="Curb Weight")
    make = fields.Char(string="Make")
    model = fields.Char(string="Model")
    year = fields.Integer(string="Year")
    launch_date = fields.Date(string="Launch Date")

    # Adds a new type for motorcycles and set its behavior on deletion
    detailed_type = fields.Selection(
        selection_add=[("motorcycle", "Motorcycle")],
        ondelete={"motorcycle": "set default"},
        help="Motorcycles go brrrrrrrr.",
    )

    # Override method to map detailed types
    def _detailed_type_mapping(self):
        # Call super method to get mapping from parent class
        type_mapping = super()._detailed_type_mapping()
        # Add motorcycle type mapping to the existing mapping
        type_mapping["motorcycle"] = "product"
        return type_mapping

    # detailed_type
    #   This field represents the detailed type of the product, categorized as 'Consumable' or 'Service'.
    # type
    #   This field is computed based on the value of detailed_type. It represents the type of the product, with options 'Consumable' or 'Service'.
    # Relation:
    #   The relation between detailed_type and type is established through the _compute_type method, which is decorated with @api.depends('detailed_type').
    #   This decorator indicates that the computation of the type field depends on the value of detailed_type.
    #   Inside the _compute_type method, a type_mapping dictionary is created using the _detailed_type_mapping method.
    #   This method seems to be a custom method defined within the model or its superclass to provide a mapping between detailed types and their corresponding types.
