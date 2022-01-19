# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class TransacaoOriginal(models.TransientModel):
    _name = 'desafiobc.transacao'
    _description = 'Transacão - movimentos de entrada / saída referente às lojas'
    _order = 'id'

    # sequencial = fields.Integer()
    tipo_transacao_id = fields.Many2one('desafiobc.tipo.transacao', string='Tipo Transação',
                                 # optional:
                                 ondelete='restrict',
                                 context={},
                                 domain=[],
                                 )
    data_hora_ocorrencia = fields.Datetime()
    valor_movimentacao = fields.Float('Valor',  digits=(10,2), )
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
    dono_loja_id = fields.Many2one('desafiobc.dono.loja', string='Dono da Loja',
                                 # optional:
                                 ondelete='restrict',
                                 context={},
                                 domain=[],
                                 )

