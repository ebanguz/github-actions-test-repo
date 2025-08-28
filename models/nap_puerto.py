from odoo import models, fields, api


class NapPuerto(models.Model):
	_name = 'nap.puerto'
	_description = 'Puerto de Caja NAP'

	name = fields.Char(string="Nombre", required=True, default="Puerto NAP")
	numero = fields.Integer(string="Código", required=True)
	ocupado = fields.Boolean(
		string="Estado Ocupado",
		default=False,
		compute='_compute_estado',
		store=True
	)
	is_ocupado = fields.Char(
		string="Ocupado",
		default='Disponible',
		compute='_compute_estado',
		store=True
	)
	color = fields.Integer(string="Color", compute='_compute_estado', store=True)

	# Relations
	caja_id = fields.Many2one('nap.caja', string="Caja NAP", ondelete="set null")
	cliente_id = fields.Many2one(
		'res.partner',
		string="Cliente",
		ondelete="set null",
		domain="[('mkw_status', '=', 'activo')]"
	)
	contract_id = fields.Many2one(
		'subscription.contracts',
		string="Contrato",
		domain="[('partner_id', '=', cliente_id)]"
	)
	# Related fields
	status_of_cliente_id = fields.Selection(
		related='cliente_id.mkw_status',
		string="Estado del Cliente",
		readonly=True,
		store=True
	)
	active_of_cliente_id = fields.Boolean(
		related='cliente_id.active',
		string="Activo del Cliente",
		readonly=True,
		store=True
	)

	@api.depends('ocupado')
	def _compute_color( self ):
		for rec in self:
			rec.color = 1 if rec.ocupado else 10
			rec.is_ocupado = 'Ocupado' if rec.ocupado else 'Disponible'

	# Single compute method for all dependent fields
	@api.depends('cliente_id', 'cliente_id.mkw_status', 'cliente_id.active')
	def _compute_estado( self ):
		for rec in self:
			rec.ocupado = bool(rec.cliente_id)
			rec.is_ocupado = 'Ocupado' if rec.ocupado else 'Disponible'
			rec.color = 1 if rec.ocupado else 10
