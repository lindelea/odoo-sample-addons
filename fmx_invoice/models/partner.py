# -*- coding: utf-8 -*-

from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    invoice_jp_no = fields.Char('適格請求書登録番号')
