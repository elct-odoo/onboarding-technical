# -*- coding: utf-8 -*-

import re

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class motorcycle_registry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registry_number"

    certificate_title = fields.Binary(string="Certificate Title")
    current_mileage = fields.Float(string="Current Mileage")
    date_registry = fields.Date(string="Date of Registry")
    license_plate = fields.Char(string="License Plate")
    registry_number = fields.Char(
        string="Registry Number",
        copy=False,
        required=True,
        readonly=True,
        default="MRN0000",
    )
    vin = fields.Char(string="VIN", required=True)

    owner_id = fields.Many2one(
        comodel_name="res.partner", ondelete="restrict", string="Owner"
    )
    owner_phone = fields.Char(related="owner_id.phone", readonly=True)
    owner_email = fields.Char(related="owner_id.email", readonly=True)

    make = fields.Char(compute="_compute_make", readonly=True)
    model = fields.Char(compute="_compute_model", readonly=True)
    year = fields.Char(compute="_compute_year", readonly=True)

    @api.depends("vin")
    def _compute_make(self):
        for registry in self:
            if registry.vin:
                registry.make = registry.vin[:2]
            else:
                registry.make = False

    @api.depends("vin")
    def _compute_model(self):
        for registry in self:
            if registry.vin:
                registry.model = registry.vin[2:4]
            else:
                registry.model = False

    @api.depends("vin")
    def _compute_year(self):
        for registry in self:
            if registry.vin:
                registry.year = registry.vin[4:6]
            else:
                registry.year = False

    @api.constrains("license_plate")
    def _check_license_plate_size(self):
        pattern = "^[A-Z]{1,3}\d{1,4}[A-Z]{0,2}$"
        for registry in self.filtered(lambda r: r.license_plate):
            match = re.match(pattern, registry.license_plate)
            if not match:
                raise ValidationError(_("Invalid License Plate"))

    @api.constrains("vin")
    def _check_vin_pattern(self):
        pattern = "^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}$"
        for registry in self.filtered(lambda r: r.vin):
            match = re.match(pattern, registry.vin)
            if not match:
                raise ValidationError(_("Invalid VIN"))
            if not registry.vin[0:2] == "KA":
                raise ValidationError(
                    _("Only motorcycles from Kawill Motors are allowed")
                )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if "registry_number" not in vals:
                vals["registry_number"] = self.env["ir.sequence"].next_by_code(
                    "registry.number"
                )
        return super().create(vals_list)
