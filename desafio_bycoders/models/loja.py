# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api


_logger = logging.getLogger(__name__)

class Loja(models.TransientModel):
    _name = 'desafiobc.loja'
    _description = 'Loja'

    name = fields.Char('Nome da loja')
    saldo = fields.Float('Saldo',  digits=(10,2), )

    dono_loja_ids = fields.One2many('desafiobc.dono.loja', "loja_id", string="Dono Loja")
    transacao_ids = fields.One2many('desafiobc.transacao', "loja_id", string="Transação")

    _sql_constraints = [
        ('unique_loja', 'unique(name)', 'Nome da loja deve ser único.')
    ]

