# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api


_logger = logging.getLogger(__name__)

class TransacaoOriginal(models.TransientModel):
    _name = 'desafiobc.transacao.original'
    _description = 'Transacao Original - movimentos recém importados de arquivo CNAB'
    _order = 'id'

    # sequencial = fields.Integer()
    tipo_transacao = fields.Char()
    data_ocorrencia = fields.Char()
    valor_movimentacao = fields.Char()
    cpf_beneficiario = fields.Char()
    cartao_transacao = fields.Char()
    hora_transacao = fields.Char()
    dono_loja = fields.Char()
    nome_loja = fields.Char()

