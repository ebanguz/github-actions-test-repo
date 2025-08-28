from odoo import fields, models, api


class Mufa(models.Model):
	_name = 'nap.mufa'
	_description = 'Description of the model Mufa'

	name = fields.Char(string="Código", required=True)
	coordenadas = fields.Char(string="Coordenadas URL", required=True, default="https://www.google.com/maps",
	                          help="Coordenadas de la caja en formato: Latitud, Longitud")
	latitud = fields.Char(string="Latitud")
	longitud = fields.Char(string="Longitud")

	splitter_id = fields.One2many('nap.splitter', 'mufa_id', string="Splitter")
