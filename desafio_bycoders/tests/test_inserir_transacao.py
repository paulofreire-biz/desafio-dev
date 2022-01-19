from odoo.tests.common import TransactionCase
import logging

_logger = logging.getLogger(__name__)

class TestInserirTransacao(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestInserirTransacao, self).setUp(*args, **kwargs)
        linha = '3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       '
        rec = self.env['desafiobc.importar.arquivo'].salvar_linha(linha)
        self.test_transacao = self.env['desafiobc.importar.arquivo'].inserir_transacao(rec)

    def test_valor_movimentacao(self):
        _logger.info('self.test_transacao.valor_movimentacao = %s', abs(self.test_transacao.valor_movimentacao))
        self.assertEqual(abs(self.test_transacao.valor_movimentacao), 142,
                         'Deveria ter encontrado um valor de movimentação igual a 142,00!')

