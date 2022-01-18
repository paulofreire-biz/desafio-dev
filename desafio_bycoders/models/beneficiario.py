# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api


_logger = logging.getLogger(__name__)

class Beneficiario(models.TransientModel):
    _name = 'desafiobc.beneficiario'
    _description = 'Beneficiário'

    cpf = fields.Char('CPF')

    _sql_constraints = [
        ('unique_cpf', 'unique(cpf)', 'CPF deve ser único.')
    ]


