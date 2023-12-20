# -*- coding: utf-8 -*-

from odoo import models, fields, api

class nitro_custom3(models.Model):
    
    _inherit = 'nitro.gas.stacion'

    #Valores para la venta
    _fovial = fields.Float(default="0.20")
    _iva = fields.Float(default="0.13")
    _neto = fields.Float(default='0')
    _total_sale = fields.Float(compute='_get_sum')
    _neto_sale = fields.Float(0)

    #Valor del Producto
    _price_regular = fields.Float("4.5")
    _price_sueper = fields.Float("5.5")
    _price_diesel = fields.Float("6.5")

    #Tipo de Producto
    _regular = fields.Boolean(string="Gasolina Regular")
    _super = fields.Boolean(string="Gasolina Super")
    _diesel = fields.Boolean(string="Diesel")

    @api.onchange('_regular','_super','_diesel','_neto')
    def _gasselect(self):
        if self._regular == True:
            self._super = False
            self._diesel = False
            #self._neto_sale = _price_regular
        elif self._super == True:
            self._diesel = False
            self._regular = False
            #self._neto_sale = _price_sueper
        elif self._diesel == True:
            self._regular = False
            self._super = False
            #self._neto_sale = _price_diesel
        else:
            self._regular = False
            self._super = False
            self._diesel = False
            self._neto_sale = 0

    @api.onchange('_regular','_super','_diesel')
    def _gasselect2(self):
        if self._regular == False and self._super == False:
            self._diesel = True
        elif self._super == False and self._diesel == False:
            self._regular = True
        else:
            self._super = True
            self._regular = False
            self._diesel = False

    @api.constrains('_regular')
    def _regulars(self):
        if self._regular == True:
            self._super = False
            self._diesel = False

    @api.constrains('_super')
    def _supers(self):
        if self._super == True:
            self._regular = False
            self._diesel = False

    @api.constrains('_diesel')
    def _diesels(self):
        if self._diesel == True:
            self._super = False
            self._regular = False

    @api.depends('_total_sale', '_neto', '_iva', '_fovial')
    def _get_sum(self):
        for rec in self:
          rec._total_sale = rec._neto+rec._iva+rec._fovial

