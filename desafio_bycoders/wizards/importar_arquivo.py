# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api
from datetime import datetime

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

        if (self.env['desafiobc.transacao'].search_count([['id', '>', 0]])) == 0:
            _logger.info('Vai carregar_transacao')
            self.carregar_transacao()

    # A função abaixo tem como objetivo pegar os dados da transacao.original e copiar para transacao
    def carregar_transacao(self):

        vals = {}
        lista_transacao = self.env['desafiobc.transacao.original'].search([['id', '>', 0]])
        for rec in lista_transacao:
            date_time_str = rec.data_ocorrencia+rec.hora_transacao
            date_time_obj = datetime.strptime(date_time_str, '%Y%m%d%H%M%S')
            vals['data_hora_ocorrencia'] = date_time_obj

            # Validando se o tipo da transação existe
            tipo_transacao = self.env['desafiobc.tipo.transacao'].search([['tipo_transacao', '=', int(rec.tipo_transacao)]])
            if not tipo_transacao:
                # Não encontrou a transação correspondente, neste caso iremos abandonar esta transação
                vals2 = {}
                vals2['registro_ok'] = False
                rec.write(vals2)
                continue

            vals['tipo_transacao_id'] = tipo_transacao.id

            valor_movimentacao = int(rec.valor_movimentacao)/100
            if not tipo_transacao.is_natureza_entrada:
                valor_movimentacao = valor_movimentacao * (-1)

            vals['valor_movimentacao'] = valor_movimentacao

            # Tratando beneficiario
            beneficiario = self.env['desafiobc.beneficiario'].search([['cpf', '=', rec.cpf_beneficiario]])
            # Verificando se beneficiário já existe, caso contrário iremos inserí-lo
            _logger.info('beneficiario = %s', beneficiario)
            if not beneficiario:
                vals2 = [{'cpf': rec.cpf_beneficiario}]
                beneficiario = self.env['desafiobc.beneficiario'].create(vals2)

            vals['beneficiario_id'] = beneficiario.id

            # Tratando cartão
            cartao = self.env['desafiobc.cartao'].search([['cartao', '=', rec.cartao_transacao]])
            # Verificando se cartão já existe, caso contrário iremos inserí-lo
            if not cartao:
                vals2 = [{'cartao': rec.cartao_transacao}]
                cartao = self.env['desafiobc.cartao'].create(vals2)

            vals['cartao_id'] = cartao.id

            # Tratando loja
            loja = self.env['desafiobc.loja'].search([['name', '=', rec.nome_loja]])
            # Verificando se loja já existe, caso contrário iremos inserí-la
            if not loja:
                vals2 = [{'name': rec.nome_loja}]
                loja = self.env['desafiobc.loja'].create(vals2)

            _logger.info('tipo_transacao.is_natureza_entrada = %s', tipo_transacao.is_natureza_entrada)
            # Atualizando o saldo da loja
            # valor_atualizacao = valor_movimentacao if tipo_transacao.is_natureza_entrada else valor_movimentacao * (-1)
            vals2 = {}
            vals2['saldo'] = loja.saldo + valor_movimentacao
            loja.write(vals2)

            vals['loja_id'] = loja.id

            # Tratando dono da loja para a loja corrente (estou admitindo a possibilidade de um dono possuir mais de uma loja)
            dono_loja = self.env['desafiobc.dono.loja'].search([['loja_id', '=', loja.id],['name', '=', rec.dono_loja]])
            # Verificando se dono da loja já existe, caso contrário iremos inserí-lo
            if not dono_loja:
                vals2 = [{'loja_id': loja.id, 'name': rec.dono_loja}]
                dono_loja = self.env['desafiobc.dono.loja'].create(vals2)

            vals['dono_loja_id'] = dono_loja.id

            # Inserindo nova transação
            transacao = self.env['desafiobc.transacao'].create(vals)

            # Se chegamos até aqui é porque foi tudo bem, atualizando o nosso flag...
            vals2 = {}
            vals2['registro_ok'] = True
            rec.write(vals2)

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

