# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api


_logger = logging.getLogger(__name__)

class Loja(models.TransientModel):
    _name = 'desafiobc.loja'
    _description = 'Loja'

    name = fields.Char('Nome da loja')

    dono_loja_ids = fields.One2many('desafiobc.dono.loja', "loja_id", string="Dono Loja")



