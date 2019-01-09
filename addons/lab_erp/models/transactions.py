# -*- coding: utf-8 -*-
from odoo import models, api, fields


class Transaction_C_M (models.Model):
    _name = 'lab_erp.transaction_c_m'

    name_trans = fields.Char(string='Name Transaction')
    order = fields.Many2one('lab_erp.order', string='Order')
    payer = fields.Char(string='Payer')
    detail = fields.Char(string='Detail')
    success_at = fields.Datetime(string='Datetime Success')
    paid = fields.Boolean(string='Paid')
    archive = fields.Boolean(string='Archive')
    cancel = fields.Boolean(string='Cancel')




class Transaction_A_M (models.Model):
    _name = 'lab_erp.transaction_a_m'
    _rec_name = 'trans_name'

    trans_name = fields.Char(string='Transaction Name')
    merchant = fields.Many2one('lab_erp.account', string='Merchant')
    amount = fields.Integer(string='Amount')
    state = fields.Selection(selection=[('1', 'Paid'), ('0', 'Not Paid')], string='State')
    success_at = fields.Datetime(string='Success at')
    archive = fields.Boolean(string='Archive')
    is_active = fields.Boolean(string='Active')
    

class Transaction_Detail_A_M (models.Model):
    _name = 'lab_erp.transaction_detail_a_m'
    

    trans_id = fields.Many2one('lab_erp.transaction', string='transaction')
    service_id = fields.Many2one('lab_erp.service', string='Service')
    quantity = fields.Integer(string='Quantity')
    # state = fields.Selection(string='State')

