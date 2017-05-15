# -*- coding: utf-8 -*-
# ATT Generated at 2017-05-05 16:10:19

from odoo import models, fields, api

class CorretivaEntryForm(models.Model):
    _name = 'corretiva.entry_form'
    _rec_name = 'entry_form_request_number'
    _sql_constraints = [('corretiva.entry_form', 'unique (entry_xml_filename)', 'XML já foi importado anteriormente!')]

    entry_xml_filename = fields.Char(string='XML importado!!!', default='')
    entry_form_date_time = fields.Char(string='Data', default='')
    entry_date_from_epoch = fields.Char(string='Data Epoch da Entrada')
    entry_location_address = fields.Char(string='Endereço')
    entry_location_x = fields.Char(string='longitude')
    entry_location_y = fields.Char(string='latitude')
    entry_location_date = fields.Char(string='Data da Localização')
    entry_location_date_from_epoch = fields.Char(string='Data Formulário')
    entry_form_name = fields.Char(string='Formulário')
    entry_form_version = fields.Integer(string='Versão')
    entry_form_customer_number = fields.Integer(string='Nr Cliente')
    entry_form_request_number = fields.Char(string='NÚMERO DO CHAMADO')
    entry_form_checkin_pa = fields.Char(string='CHECK IN - PA TÉCNICA')
    entry_form_checkout_pa = fields.Char(string='CHECK OUT - PA TÉCNICA')
    entry_form_fault_info_service_now = fields.Char(string='PROBLEMA INFORMADO SERVICE NOW')
    entry_form_ocurred_fault = fields.Char(string='PROBLEMA OCORRIDO')
    entry_form_action_done = fields.Char(string='AÇÃO REALIZADA')
    entry_form_station_responsible_name = fields.Char(string='NOME DO RESPONSÁVEL DO POSTO')
    entry_form_station_responsible_email = fields.Char(string='EMAIL DO RESPONSÁVEL DO POSTO')
    entry_form_station_email_group = fields.Char(string='Grupo E-mail')
    entry_form_station_email_sendto = fields.Char(string='E-mail Para')
    entry_form_employee_firstname = fields.Char(string='Nome do Funcionário')
    entry_form_employee_email = fields.Char(string='Email do Funcionário')
    entry_form_employee_number = fields.Char(string='Nr. do Funcionário')
    entry_form_employee_driver_id = fields.Integer(string='Código do Motorista')
    entry_form_employee_group_name = fields.Char(string='Grupo do Funcionário')
    entry_form_poi_customer_city = fields.Char(string='Cidade')
    entry_form_poi_customer_number = fields.Integer(string='Código do Posto')
    entry_form_poi_customer_name = fields.Char(string='Nome do Posto')
    entry_form_poi_customer_street = fields.Char(string='Endereço')
    entry_form_ref_poi_layer_name = fields.Char(string='Nome da Camada')
    entry_form_file_ids = fields.One2many('corretiva.entry_form_files', 'entry_form_file_id', u'Form id')
    entry_form_perf_add_ids = fields.One2many('corretiva.entry_form_perf_add', 'entry_form_perf_add_id', u'Form Id')
    entry_form_perf_rem_ids = fields.One2many('corretiva.entry_form_perf_rem', 'entry_form_perf_rem_id', u'Form Id')

class CorretivaEntryFormFiles(models.Model):
    _name = 'corretiva.entry_form_files'
    _rec_name = 'entry_form_file_description'

    entry_form_file_description = fields.Char(string='Descrição da Foto')
    entry_form_file_data = fields.Binary(string='Foto')
    entry_form_file_id = fields.Many2one('corretiva.entry_form', u'Fotos', ondelete='cascade', required=True)

class CorretivaEntryFormPerfsAdd(models.Model):
    _name = 'corretiva.entry_form_perf_add'
    _rec_name = 'entry_form_perf_item'

    entry_form_perf_action = fields.Char(string='PERF_ACTION', default='PERF_REM')
    entry_form_perf_item = fields.Char(string='PERF_ITEM')
    entry_form_perf_l_inst = fields.Char(string='PERF_ITEM_L_INST')
    entry_form_perf_num_serial = fields.Char(string='PERF_ITEM_NUM_SERIAL')
    entry_form_perf_num_pat = fields.Char(string='PERF_ITEM_NUM_PAT')
    entry_form_perf_add_id = fields.Many2one('corretiva.entry_form', u'PERF_ADD', ondelete='cascade', required=True)

class CorretivaEntryFormPerfsRem(models.Model):
    _name = 'corretiva.entry_form_perf_rem'
    _rec_name = 'entry_form_perf_item'

    entry_form_perf_action = fields.Char(string='PERF_ACTION', default='PERF_REM')
    entry_form_perf_item = fields.Char(string='PERF_ITEM')
    entry_form_perf_l_inst = fields.Char(string='PERF_ITEM_L_INST')
    entry_form_perf_num_serial = fields.Char(string='PERF_ITEM_NUM_SERIAL')
    entry_form_perf_num_pat = fields.Char(string='PERF_ITEM_NUM_PAT')
    entry_form_perf_rem_id = fields.Many2one('corretiva.entry_form', u'PERF_REM', ondelete='cascade', required=True)
