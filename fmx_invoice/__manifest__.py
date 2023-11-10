# -*- coding: utf-8 -*-
{
    'name': '日本インボイス制度対応',
    'version': '1.0',
    'author': "Fourmix inc.",
    'summary': '日本インボイス制度対応するためのシステム改修です。',
    'sequence': 10,
    'description': '令和5年（2023年）10月1日からインボイス制度が始まりました。この「インボイス」とは、事業者間でやり取りされる消費税額等が記載された請求書や領収書等のこと ...',
    'category': 'Purchases',
    'website': 'https://www.fourmix.co.jp',
    'depends': ['base', 'purchase'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
