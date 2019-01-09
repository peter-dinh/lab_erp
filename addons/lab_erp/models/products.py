# -*- coding: utf-8 -*-
from odoo import models, api, fields


class Product (models.Model):
    _name = 'lab_erp.product'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    detail = fields.Char(string='Detail')
    origin = fields.Char(string='Origin')
    merchant = fields.Many2one('lab_erp.account', string='Merchant')
    category = fields.Many2many('lab_erp.category', string='Category')
    attribute = fields.Many2many('lab_erp.product_attribute', string='Attribute')
    agv_star = fields.Float(string='Agv Star')
    total_star = fields.Integer(string='Total Star', compute='_compute_total_star')
    archive = fields.Boolean(string='Archive')
    is_active = fields.Boolean(string='Active')

    @api.multi
    def get_agv_star(self):
        print(self)

class Category(models.Model):
    _name = 'lab_erp.category'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    quantity = fields.Integer(string='Quantity', compute='get_quantity_category', store=True)
    archive = fields.Boolean(string='Archive')

    @api.multi
    def get_quantity_category(self):
        for item in self:
            list_product = item.env['lab_erp.post_product'].search([('product.category_id', '=', item.id), ('product.archive', '=', True)])
            print(list_product)


# them truong nguoi tao de nguoi do co the su dung thuoc tinh do
class Attribute (models.Model):
    _name = 'lab_erp.attribute'
    _rec_name = 'label'

    label =  fields.Char(string='Label')
    is_required = fields.Boolean(string='Required')
    is_unique = fields.Boolean(string='Unique')

class Product_Attribute (models.Model):
    _name  =  'lab_erp.product_attribute'
    _inherit = 'lab_erp.attribute'
    
    value = fields.Char(string='Value')
    archive = fields.Boolean(string='Archive')

class Discount (models.Model):
    _inherit = 'lab_erp.product'
    
    percent = fields.Integer(string='Percent')
    price_origin = fields.Integer(string='Price Origin')
    price_sales = fields.Integer(string='Price Sales')
    date_start = fields.Datetime(string='Date start')  
    date_end = fields.Datetime(string='Date end')
    archive = fields.Boolean(string='Archive')

    @api.onchange('price_sales')
    def get_percent_discount(self):
        if not self.price_origin: return 
        else:
            if self.price_sales > self.price_origin:
                return 
            else:
                self.percent = int((self.price_origin - self.price_sales) / self.price_origin)

class Rating (models.Model):
    _name = 'lab_erp.rating'

    customer = fields.Many2one('lab_erp.account', string='Customer')
    num_of_star = fields.Integer(string='Start')
    comment = fields.Char(string='Comment')
    product = fields.Many2one('lab_erp.product', string='Product')
    is_active = fields.Boolean(string='Active')


    # @api.constrains('customer')
    # def _check_customer_buyed_product(self):
    #     for record in self:
            
            
    