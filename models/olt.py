from odoo import fields, models, api


class OLT(models.Model):
	_name = 'nap.olt'
	_description = 'Description of OLP Model'

	name = fields.Char(string="Codigo", required=True)
