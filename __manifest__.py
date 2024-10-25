{
    'name': 'Room Booking System',
    'version': '1.0',
    'summary': 'Modul Pemesanan Ruangan',
    'description': 'Modul untuk mengelola pemesanan ruangan dan master ruangan.',
    'author': 'boy',
    'category': 'Operations',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/room_sequence.xml',
        'views/room_views.xml',
        'views/booking_views.xml'
    ],
    'installable': True,
    'application': True,
}
