# -*- coding: utf-8 -*-
from odoo import http


class Login(http.Controller):
    @http.route('/login/', auth='public')
    def login(self, **kw):
        return "Demo"