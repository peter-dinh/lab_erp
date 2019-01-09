from odoo import http

class Index(http.Controller):
    @http.route('/', auth="public")
    def index():
        return