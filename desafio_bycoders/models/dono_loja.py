# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api


_logger = logging.getLogger(__name__)

class DonoLoja(models.TransientModel):
    _name = 'desafiobc.dono.loja'
    _description = 'Dono da Loja'

    name = fields.Char('Dono da loja')

    loja_id = fields.Many2one('desafiobc.loja', string='Loja',
                                 # optional:
                                 ondelete='restrict',
                                 context={},
                                 domain=[],
                                 )

    _sql_constraints = [
        ('unique_dono_loja', 'unique(loja_id, name)', 'Nome dono loja deve ser único para determinada loja.')
    ]




