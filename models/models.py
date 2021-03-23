# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Alumno(models.Model):
     _name = 'convalidaciones.alumno'

     name = fields.Char(string="Nombre y Apellidos")
     edad = fields.Integer(string="Edad")

class Modulo(models.Model):
     _name = 'convalidaciones.modulo'

     name = fields.Char(string="Nombre")
     description = fields.Text(string="Descripcion")

class Convalidacion(models.Model):
     _name = 'convalidaciones.convalidacion'

     name = fields.Char()
     fecha_convalidacion = fields.Date(string="Fecha de la convalidacion")
     modulo_id = fields.Many2one('convalidaciones.modulo', string="Modulo")
     alumno_id = fields.Many2one('convalidaciones.alumno', string="Alumno")