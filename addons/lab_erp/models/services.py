# -*- coding: utf-8 -*-
from odoo import models, api, fields


class Service (models.Model):
    _name = 'lab_erp.service'
    _rec_name = 'service_name'

    service_name = fields.Char(string='Service Name')
    amount = fields.Integer(string='Amount')
    value  = fields.Char(string='Value')
    unit = fields.Char(string='Unit')
    is_active = fields.Boolean(string='Actvie')
    archive = fields.Boolean(string='Archive')