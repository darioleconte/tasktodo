# -*- coding: utf-8 -*-
# from odoo import http


# class Tasktodo(http.Controller):
#     @http.route('/tasktodo/tasktodo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tasktodo/tasktodo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tasktodo.listing', {
#             'root': '/tasktodo/tasktodo',
#             'objects': http.request.env['tasktodo.tasktodo'].search([]),
#         })

#     @http.route('/tasktodo/tasktodo/objects/<model("tasktodo.tasktodo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tasktodo.object', {
#             'object': obj
#         })
