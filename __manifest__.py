{
    'name': 'Room Booking System',
    'version': '1.0',
    'summary': 'Modul Pemesanan Ruangan',
    'description': 'Modul untuk mengelola pemesanan ruangan dan master ruangan.',
    'author': 'boy',
    'category': 'Operations',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['base','mail'],
    'data': [
        'views/room_booking_views.xml',
        'views/master_ruangan_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
