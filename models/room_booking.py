from odoo import models, fields

class PemesananRuangan(models.Model):
    _name = 'room.booking'
    _description = 'Pemesanan Ruangan'

    booking_number = fields.Char(string='Nomor Pemesanan', required=True)
    room_id = fields.Many2one('room.master', string='Ruangan', required=True)
    booking_name = fields.Char(string='Nama Pemesan', required=True)
    booking_date = fields.Date(string='Tanggal Pemesanan', required=True)
    status = fields.Selection([('draft', 'Draft'), ('on_going', 'On Going'), ('done', 'Done')], string='Status', default='draft')
    notes = fields.Text(string='Catatan')
