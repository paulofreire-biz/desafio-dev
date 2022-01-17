# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class TransacaoOriginal(models.TransientModel):
    _name = 'desafiobc.transacao.original'
    _description = 'Transacao Original - movimentos recém importados de arquivo CNAB'
    _order = 'id'

    # sequencial = fields.Integer()
    tipo_transacao_id = fields.Many2one('desafiobc.tipo.transacao', string='Tipo Transação',
                                 # optional:
                                 ondelete='restrict',
                                 context={},
                                 domain=[],
                                 )
    data_hora_ocorrencia = fields.Date()
    valor_movimentacao = fields.Monetary('Valor')
    beneficiario_id = fields.Many2one('desafiobc.beneficiario', string='Beneficiário',
                                 # optional:
                                 ondelete='restrict',
                                 context={},
                                 domain=[],
                                 )
    cartao_id = fields.Many2one('desafiobc.cartao', string='Cartão',
                                 # optional:
                                 ondelete='restrict',
                                 context={},
                                 domain=[],
                                 )
    loja_id = fields.Many2one('desafiobc.loja', string='Loja',
                                 # optional:
                                 ondelete='restrict',
                                 context={},
                                 domain=[],
                                 )
    dono_loja_id = fields.Many2one('desafiobc.dono.loja', string='Loja',
                                 # optional:
                                 ondelete='restrict',
                                 context={},
                                 domain=[],
                                 )

