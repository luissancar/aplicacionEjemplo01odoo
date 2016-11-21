#-*- coding: utf-8 -*-
from openerp import models, fields

class Aplicacionejemplo01Task(models.Model):
    #_name debe ser el nombre de la clase empezando en minúscula
    # y al comienzo de otra mayúscula poner punto y ésta en minuscula
    _name = 'aplicacionejemplo01.task'
    name = fields.Char('Description', required=True)
    name2 = fields.Char('Description2', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)