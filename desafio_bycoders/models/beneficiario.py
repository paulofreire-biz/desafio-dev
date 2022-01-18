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

    def name_get(self):
        """ This method is used to customize display name of the record. In this case we are overriding the name_get method """
        result = []
        for rec in self:
            result.append((rec.id, rec.cpf))
        return result
