# -*- coding: utf-8 -*-
# from odoo import http


# class MotorcycleRegistry(http.Controller):
#     @http.route('/motorcycle_registry/motorcycle_registry', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/motorcycle_registry/motorcycle_registry/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('motorcycle_registry.listing', {
#             'root': '/motorcycle_registry/motorcycle_registry',
#             'objects': http.request.env['motorcycle_registry.motorcycle_registry'].search([]),
#         })

#     @http.route('/motorcycle_registry/motorcycle_registry/objects/<model("motorcycle_registry.motorcycle_registry"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('motorcycle_registry.object', {
#             'object': obj
#         })
