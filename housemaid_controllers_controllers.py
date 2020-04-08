# -*- coding: utf-8 -*-
# from odoo import http


# class Housemaid(http.Controller):
#     @http.route('/housemaid/housemaid/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/housemaid/housemaid/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('housemaid.listing', {
#             'root': '/housemaid/housemaid',
#             'objects': http.request.env['housemaid.housemaid'].search([]),
#         })

#     @http.route('/housemaid/housemaid/objects/<model("housemaid.housemaid"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('housemaid.object', {
#             'object': obj
#         })
