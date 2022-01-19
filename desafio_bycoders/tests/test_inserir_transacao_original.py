from odoo.tests.common import TransactionCase

class TestInserirTransacaoOriginal(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestInserirTransacaoOriginal, self).setUp(*args, **kwargs)
        linha = '3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       '
        self.test_transacao_original = self.env['desafiobc.importar.arquivo'].salvar_linha(linha)

    def test_tipo_transacao(self):
        self.assertEqual(self.test_transacao_original.tipo_transacao, '3',
                         'Deveria ter encontrado um Tipo de Transação igual a 3!')

