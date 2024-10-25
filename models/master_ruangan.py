from odoo import models, fields

class MasterRuangan(models.Model):
    _name = 'room.master'
    _description = 'Master Ruangan'

    name = fields.Char(string='Nama Ruangan', required=True)
    room_type = fields.Selection([('small_meeting', 'Meeting Room Kecil'),
                                  ('large_meeting', 'Meeting Room Besar'),
                                  ('aula', 'Aula')], string='Tipe Ruangan', required=True)
    location = fields.Selection([('1A', '1A'), ('1B', '1B'), ('1C', '1C'),
                                 ('2A', '2A'), ('2B', '2B'), ('2C', '2C')], string='Lokasi', required=True)
    photo = fields.Binary(string='Foto Ruangan', required=True)
    capacity = fields.Integer(string='Kapasitas', required=True)
    description = fields.Text(string='Keterangan')
