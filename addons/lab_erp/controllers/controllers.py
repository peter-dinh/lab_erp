# -*- coding: utf-8 -*-
from odoo import http

# class LabErp(http.Controller):
#     @http.route('/lab_erp/lab_erp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lab_erp/lab_erp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lab_erp.listing', {
#             'root': '/lab_erp/lab_erp',
#             'objects': http.request.env['lab_erp.lab_erp'].search([]),
#         })

#     @http.route('/lab_erp/lab_erp/objects/<model("lab_erp.lab_erp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lab_erp.object', {
#             'object': obj
#         })