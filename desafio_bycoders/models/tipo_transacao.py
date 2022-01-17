# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api


_logger = logging.getLogger(__name__)

class TipoTransacao(models.TransientModel):
    _name = 'desafiobc.tipo.transacao'
    _description = 'Tipo de Transação'
    _order = 'id'

    # sequencial = fields.Integer()
    tipo_transacao = fields.Integer()
    descricao = fields.Char()
    is_natureza_entrada = fields.Boolean()

    natureza = fields.Char(compute='_compute_natureza')
    sinal = fields.Char(compute='_compute_sinal')

    @api.depends('tipo_transacao')
    def _compute_natureza(self):
        for rec in self:
            rec.natureza = 'Entrada' if rec.is_natureza_entrada else 'Saída'

    @api.depends('tipo_transacao')
    def _compute_sinal(self):
        for rec in self:
            rec.sinal = '+' if rec.is_natureza_entrada else '-'

    def carregar_tabela(self):

        vals = {}
        vals['tipo_transacao'] = 1
        vals['descricao'] = 'Débito'
        vals['is_natureza_entrada'] = False
        self.create(vals)

        vals['tipo_transacao'] = 2
        vals['descricao'] = 'Boleto'
        vals['is_natureza_entrada'] = False
        self.create(vals)

        vals['tipo_transacao'] = 3
        vals['descricao'] = 'Financiamento'
        vals['is_natureza_entrada'] = False
        self.create(vals)

        vals['tipo_transacao'] = 4
        vals['descricao'] = 'Crédito'
        vals['is_natureza_entrada'] = True
        self.create(vals)

        vals['tipo_transacao'] = 5
        vals['descricao'] = 'Recebimento Empréstimo'
        vals['is_natureza_entrada'] = True
        self.create(vals)

        vals['tipo_transacao'] = 6
        vals['descricao'] = 'Vendas'
        vals['is_natureza_entrada'] = True
        self.create(vals)

        vals['tipo_transacao'] = 7
        vals['descricao'] = 'Recebimento TED'
        vals['is_natureza_entrada'] = True
        self.create(vals)

        vals['tipo_transacao'] = 8
        vals['descricao'] = 'Recebimento DOC'
        vals['is_natureza_entrada'] = True
        self.create(vals)

        vals['tipo_transacao'] = 9
        vals['descricao'] = 'Aluguel'
        vals['is_natureza_entrada'] = False
        self.create(vals)

        _logger.info('Fim carregar_tabela')

