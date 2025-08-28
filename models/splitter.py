from odoo import fields, models, api


class Splitter(models.Model):
	_name = 'nap.splitter'
	_description = 'Description of model Splitter'

	name = fields.Char(string="Código de Splitter", required=True)
	mufa_id = fields.Many2one('nap.mufa', string="Mufa", ondelete="cascade")
