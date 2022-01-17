# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api

import base64
# import StringIO

_logger = logging.getLogger(__name__)

class ImportarArquivoWizard(models.TransientModel):
    _name = 'desafiobc.importar.arquivo'
    _description = 'Wizar para fazer o upload do arquivo e depois ler seus dados'

    arquivo_txt = fields.Binary(string='Arquivo .txt para importação', required=True)

    def inicio_processamento(self):
        _logger.info('Estou em importar_arquivo')

        if (self.env['desafiobc.transacao.original'].search_count([['id', '>', 0]])) == 0:
            _logger.info('Vai importar_arquivo')
            self.importar_arquivo()

        tipo_transacao = self.env['desafiobc.tipo.transacao']
        if (tipo_transacao.search_count([['id', '>', 0]])) == 0:
            _logger.info('Vai chamar tipo_transacao.carregar_tabela()')
            tipo_transacao.carregar_tabela()

    # def processar_transacao(self):

    def importar_arquivo(self):
        _logger.info('Estou em importar_arquivo')

        file_content = base64.decodestring(self.arquivo_txt)
        file_content = file_content.decode("utf-8")
        file_lines = file_content.split("\r\n")

        _logger.info('file_lines = %s', file_lines)

        vals = {}

        for linha in file_lines:
            _logger.info('linha = %s', linha)

            vals['tipo_transacao'] = linha[0:1]
            vals['data_ocorrencia'] = linha[1:9]
            vals['valor_movimentacao'] = linha[9:19]
            vals['cpf_beneficiario'] = linha[19:30]
            vals['cartao_transacao'] = linha[30:42]
            vals['hora_transacao'] = linha[42:48]
            vals['dono_loja'] = linha[48:62]
            vals['nome_loja'] = linha[62:81]

            transacao_original = self.env['desafiobc.transacao.original'].create(vals)
            _logger.info('Inseriu ... %s', transacao_original.id)

