# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api


_logger = logging.getLogger(__name__)

class TransacaoOriginal(models.TransientModel):
    _name = 'desafiobc.transacao.original'
    _description = 'Transacao Original - movimentos recém importados de arquivo CNAB'
    _order = 'id'

    # sequencial = fields.Integer()
    tipo_transacao = fields.Char(required=True)
    data_ocorrencia = fields.Char(required=True)
    valor_movimentacao = fields.Char(required=True)
    cpf_beneficiario = fields.Char(required=True)
    cartao_transacao = fields.Char(required=True)
    hora_transacao = fields.Char(required=True)
    dono_loja = fields.Char(required=True)
    nome_loja = fields.Char(required=True)
    registro_ok = fields.Boolean(required=False)

