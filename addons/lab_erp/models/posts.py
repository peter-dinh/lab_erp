# -*- coding: utf-8 -*-
from odoo import models, api, fields

class Post_Product (models.Model):
    _name = 'lab_erp.post_product'

    product = fields.Many2one('lab_erp.product', string='Product')
    quantity = fields.Integer(string='Quantity')
    created = fields.Datetime(string='Created')
    sponsored = fields.Boolean(string='Sponsored')
    is_push = fields.Boolean(string='Is Push')
    is_active = fields.Boolean(string='Active')
