# -*- coding: utf-8 -*-
# from odoo import http


# class DesafioBycoders(http.Controller):
#     @http.route('/desafio_bycoders/desafio_bycoders/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/desafio_bycoders/desafio_bycoders/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('desafio_bycoders.listing', {
#             'root': '/desafio_bycoders/desafio_bycoders',
#             'objects': http.request.env['desafio_bycoders.desafio_bycoders'].search([]),
#         })

#     @http.route('/desafio_bycoders/desafio_bycoders/objects/<model("desafio_bycoders.desafio_bycoders"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('desafio_bycoders.object', {
#             'object': obj
#         })
