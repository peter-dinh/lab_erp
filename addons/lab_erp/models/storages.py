# -*- coding: utf-8 -*-
from odoo import models, api, fields



# class Storage (models.Model):
#     _name = 'lab_erp.storage'

#     order = fields.Many2one('lab_erp.order', string='Order')
#     total_amount = fields.Integer(string='Total amount')
#     state = fields.Selection([()])
#     is_active = fields.Boolean(string='Active')
#     archive = fields.Boolean(string='Archive')

# class Storage_Detail (models.Model):
#     _name = 'storage_detail' 

#     storage = fields.Many2one('lab_erp.storage_detail', string='Storage')
#     product = fields.Many2one('lab_erp.product', string='Prodcut')
#     merchant = fields.Many2one('lab_erp.account', string='Merchant')
#     deli_insure_cost = fields.Integer(string='Delivery and Insure Cost')
#     state = fields.Selection([()])
#     is_active = fields.Boolean(string='Active')
#     archive = fiedls.Boolean(string='Archive')

# Can co bang xu ly san pham bi hu hong , kien cao.