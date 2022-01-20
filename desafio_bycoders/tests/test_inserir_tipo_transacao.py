from odoo.tests.common import TransactionCase
import logging

_logger = logging.getLogger(__name__)

class TestInserirTipoTransacao(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestInserirTipoTransacao, self).setUp(*args, **kwargs)
        vals = {}
        # Estamos utilizando um valor bem diferente dos já existentes, evitando assim erro de PK.
        vals['tipo_transacao'] = 99999
        vals['name'] = 'Débito'
        vals['is_natureza_entrada'] = False
        self.test_importar_arquivo = self.env['desafiobc.tipo.transacao'].create(vals)

    def test_tipo_transacao(self):
        self.assertEqual(self.test_importar_arquivo.tipo_transacao, 99999,
                         'Deveria ter encontrado um tipo de transação igual a 99999!')

