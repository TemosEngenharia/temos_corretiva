# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CorretivaTask(models.Model):
    _name = 'corretiva.task'
    _rec_name = 'request_number'

    request_number = fields.Char(string=u'Número do Chamado')
    request_open = fields.Datetime(string='Abertura do Chamado')
    request_close = fields.Datetime(string='Fechamento do Chamado')
    request_short_description = fields.Char(string='Arvore de falha')
    request_description = fields.Char(string='Descrição do erro')
    request_posto_id = 
    request_report_ids = 
