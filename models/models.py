# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class qweb-without-control-panel(models.Model):
#     _name = 'qweb-without-control-panel.qweb-without-control-panel'
#     _description = 'qweb-without-control-panel.qweb-without-control-panel'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
