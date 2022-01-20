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
    name = fields.Char('Descrição')
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

    _sql_constraints = [
        ('unique_tipo_transacao', 'unique(tipo_transacao)', 'Tipo da transação deve ser único.')
    ]

    def carregar_tabela(self):

        vals = {}
        vals['tipo_transacao'] = 1
        vals['name'] = 'Débito'
        vals['is_natureza_entrada'] = True
        self.create(vals)

        vals['tipo_transacao'] = 2
        vals['name'] = 'Boleto'
        vals['is_natureza_entrada'] = False
        self.create(vals)

        vals['tipo_transacao'] = 3
        vals['name'] = 'Financiamento'
        vals['is_natureza_entrada'] = False
        self.create(vals)

        vals['tipo_transacao'] = 4
        vals['name'] = 'Crédito'
        vals['is_natureza_entrada'] = True
        self.create(vals)

        vals['tipo_transacao'] = 5
        vals['name'] = 'Recebimento Empréstimo'
        vals['is_natureza_entrada'] = True
        self.create(vals)

        vals['tipo_transacao'] = 6
        vals['name'] = 'Vendas'
        vals['is_natureza_entrada'] = True
        self.create(vals)

        vals['tipo_transacao'] = 7
        vals['name'] = 'Recebimento TED'
        vals['is_natureza_entrada'] = True
        self.create(vals)

        vals['tipo_transacao'] = 8
        vals['name'] = 'Recebimento DOC'
        vals['is_natureza_entrada'] = True
        self.create(vals)

        vals['tipo_transacao'] = 9
        vals['name'] = 'Aluguel'
        vals['is_natureza_entrada'] = False
        self.create(vals)

        _logger.info('Fim carregar_tabela')

