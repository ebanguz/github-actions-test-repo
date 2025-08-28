from odoo import fields, models, api


class NapCaja(models.Model):
	_name = 'nap.caja'
	_description = 'Caja Nap'

	name = fields.Char(string="Código", required=True)

	coordenadas = fields.Char(
		string="Coordenadas URL",
		required=True,
		default="https://www.google.com/maps",
		help="Coordenadas de la caja en formato: Latitud, Longitud"
	)

	latitud = fields.Char(string="Latitud")
	longitud = fields.Char(string="Longitud")

	mufa_id = fields.Many2one('nap.mufa', string="Mufa")
	pon = fields.Char(string="PON")
	board = fields.Char(string="BOARD")
	olt_id = fields.Many2one('nap.olt', string="OLT")

	cantidad_puertos = fields.Integer(
		string="Cant. Puertos",
		default=8,
		compute='_compute_cantidad_puertos',
		inverse='_inverse_cantidad_puertos',
		store=True
	)
	puerto_ids = fields.One2many('nap.puerto', 'caja_id', string="Puertos", required=True)

	@api.depends('puerto_ids')
	def _compute_cantidad_puertos( self ):
		for record in self:
			record.cantidad_puertos = len(record.puerto_ids)

	@api.onchange('cantidad_puertos')
	def _inverse_cantidad_puertos( self ):
		for record in self:
			if not isinstance(record.id, models.NewId):
				current_ports = len(record.puerto_ids)
				if record.cantidad_puertos > current_ports:
					vals_list = [{
						'name'   :f'Puerto {i}',
						'numero' :i,
						'caja_id':record.id,
					} for i in range(current_ports + 1, record.cantidad_puertos + 1)]
					self.env['nap.puerto'].create(vals_list)
				elif record.cantidad_puertos < current_ports:
					record.puerto_ids[record.cantidad_puertos:].unlink()
