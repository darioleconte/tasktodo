# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api

class tasktodo(models.Model):
    _name = 'tasktodo.tasktodo'
    _description = 'tasktodo.tasktodo'

    name = fields.Char(string='Nombre')
    value = fields.Integer(string='Codigo')
    value2 = fields.Char(string='Apellido')
    notes = fields.Text(string='Notas Internas')
    vendor_ids = fields.Many2many('res.partner', string='Vendors')
    cost_price = fields.Float(string='Costo Libro', digits='Book Price')
    date_release = fields.Date('Release Date')    
    precio = fields.Monetary(string='Precio', digits='Book Price')
    currency_id = fields.Many2one('res.currency', string='Currency')
    retail_price = fields.Monetary('Retail Price') # optional attribute: currency_field='currency_id' incase currency field have another name then 'currency_id'
  #  age_days = fields.Float(string='Dias prestado', digits='Book Price')
    age_days = fields.Float(
        string='Days Since Release',
        compute='_compute_age',
        store=False,
        compute_sudo=True,
    )
    markup = fields.Float(
        string='Markup', 
        digits='Book Price',
        compute='_markup', 
        store=False,
    )
    nota1 = fields.Float(string='Nota 1', digits='Book Price')
    nota2 = fields.Float(string='Nota 2', digits='Book Price')
    nota3 = fields.Float(string='Nota 3', digits='Book Price')
    promedio = fields.Float(
        string='Promedio', 
        digits='Book Price',
        compute='_promedio', 
       # store=True,
    )

    @api.depends('date_release','cost_price','precio')
    def _compute_age(self):
        today = fields.Date.today()
        for book in self:
            if book.date_release:
                delta = today - book.date_release
                book.age_days = delta.days
            else:
                book.age_days = 0

    def _markup(self):
        ganancia = 0
        for book in self:
            if book.cost_price:
                ganancia = (book.precio - book.cost_price)
                book.markup = ganancia
            else:
                book.markup = 0
    
    def _promedio(self):
        sumatotal = 0
        for book in self:
            if book.nota1:
                sumatotal = (book.nota1 + book.nota2 + book.nota3)/3
                book.promedio = sumatotal
            else:
                book.promedio = 0