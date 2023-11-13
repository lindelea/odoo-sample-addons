# res_company.py file
from odoo import fields, models

class CustomResCompany(models.Model):
    _inherit = 'res.company'

    invoice_jp_no = fields.Char('適格請求書登録番号')
