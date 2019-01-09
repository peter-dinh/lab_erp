# -*- coding: utf-8 -*-
from odoo import models, api, fields

class Sponsored (models.Model):
    _name = 'lab_erp.sponsored'

    merchant = fields.Many2one('lab_erp.account', string='Merchant')
    transaction = fields.Many2one('lab_erp.transaction_a_m', string='Transaction')
    start = fields.Datetime(string='Start')
    end = fields.Datetime(string='End', compute='get_end_sponsored', store=True)
    active = fields.Boolean(string='Active')

    @api.multi
    def get_end_sponsored (self):
        return
