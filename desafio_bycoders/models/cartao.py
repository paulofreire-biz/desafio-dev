# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api


_logger = logging.getLogger(__name__)

class Cartao(models.TransientModel):
    _name = 'desafiobc.cartao'
    _description = 'Cartão'

    cartao = fields.Char()

    _sql_constraints = [
        ('unique_cartao', 'unique(cartao)', 'Cartão deve ser único.')
    ]

    def name_get(self):
        """ This method is used to customize display name of the record. In this case we are overriding the name_get method """
        result = []
        for rec in self:
            result.append((rec.id, rec.cartao))
        return result

