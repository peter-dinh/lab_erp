# -*- coding: utf-8 -*-
from odoo import models, api, fields

class Account (models.Model):
    _name = 'lab_erp.account'
    _inherit = 'res.users'

    # user_id = fields.Many2one('res.users', required=True, string='User')
    active_merchant = fields.Boolean(string='Active Merchant')
    sl_post = fields.Integer(compute='get_sl_post', store=True)
    sl_push = fields.Integer(compute='get_sl_push', store=True)
    sl_sponsored = fields.Integer(compute='get_sl_sponsored')

    def is_not_merchant(self):
        return

