# -*- coding: utf-8 -*-
# from odoo import http


# class Qweb-without-control-panel(http.Controller):
#     @http.route('/qweb-without-control-panel/qweb-without-control-panel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qweb-without-control-panel/qweb-without-control-panel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('qweb-without-control-panel.listing', {
#             'root': '/qweb-without-control-panel/qweb-without-control-panel',
#             'objects': http.request.env['qweb-without-control-panel.qweb-without-control-panel'].search([]),
#         })

#     @http.route('/qweb-without-control-panel/qweb-without-control-panel/objects/<model("qweb-without-control-panel.qweb-without-control-panel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qweb-without-control-panel.object', {
#             'object': obj
#         })
