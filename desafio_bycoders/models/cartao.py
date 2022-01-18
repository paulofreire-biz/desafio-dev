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

