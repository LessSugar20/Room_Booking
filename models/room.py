from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MasterRuangan(models.Model):
    _name = 'room.management'
    _description = 'Master Ruangan'

    name = fields.Char(string='Nama Ruangan', required=True)
    room_type = fields.Selection([
        ('small_meeting', 'Meeting Room Kecil'),
        ('large_meeting', 'Meeting Room Besar'),
        ('hall', 'Aula')
    ], string='Tipe Ruangan', required=True)
    location = fields.Selection([
        ('1A', '1A'), ('1B', '1B'), ('1C', '1C'),
        ('2A', '2A'), ('2B', '2B'), ('2C', '2C')
    ], string='Lokasi Ruangan', required=True)
    photo = fields.Binary(string='Foto Ruangan', required=True)
    capacity = fields.Integer(string='Kapasitas Ruangan', required=True)
    description = fields.Text(string='Keterangan')

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Nama Ruangan harus unik!')
    ]

class PemesananRuangan(models.Model):
    _name = 'room.booking'
    _description = 'Pemesanan Ruangan'

    booking_number = fields.Char(
        string='Nomor Pemesanan', required=True, copy=False, readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('room.booking')
    )
    room_id = fields.Many2one('room.management', string='Ruangan', required=True)
    booking_name = fields.Char(string='Nama Pemesanan', required=True)
    booking_date = fields.Date(string='Tanggal Pemesanan', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done')
    ], string='Status Pemesanan', default='draft', readonly=True)
    notes = fields.Text(string='Catatan Pemesanan')

    _sql_constraints = [
        ('booking_name_unique', 'unique(booking_name)', 'Nama Pemesanan harus unik!'),
        ('booking_date_room_unique', 'unique(room_id, booking_date)',
         'Tidak boleh memesan ruangan pada tanggal yang sama!')
    ]

    def action_start(self):
        self.state = 'ongoing'

    def action_done(self):
        self.state = 'done'
