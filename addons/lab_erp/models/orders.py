# -*- coding: utf-8 -*-
from odoo import models, api, fields

class Order(models.Model):
    _name = 'lab_erp.order'

    customer = fields.Many2one('lab_erp.account', string='Customer')
    amount = fields.Integer(string='Amount')
    state = fields.Selection(selection=[('0', 'Cancel'), ('1', 'Success'), ('2', 'Verified'), ('3', 'Receive order'), ('4', 'Delivery')], string='State')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    manner = fields.Selection(selection=[('0', 'COD'), ('1', 'PayPal')], string='Manner')
    verified = fields.Boolean(string='Verified')
    active = fields.Boolean(string='Active')
    archive = fields.Boolean(string='Archive')


    # @api.multi
    # def verified_order(self):
    #     if self.verified == False:

class Order_Detail (models.Model):
    _name = 'lab_erp.order_detail'

    order = fields.Many2one('lab_erp.order', string='Order')
    product = fields.Many2one('lab_erp.product', string='Product')
    merchant = fields.Many2one('lab_erp.account', string='Merchant')
    quantity = fields.Integer(string='Quantity')
    state = fields.Selection(string='State', selection=[('0', 'Cancel'), ('1', 'Success'), ('2', 'Verified'), ('3', 'Receive order'), ('4', 'Delivery')])