# -*- coding: utf-8 -*-
{
    'name': "Desafio bycoders_",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'sequence': -5,
    'description': """
        Trata-de um desafio criado pela empresa bycoders_ onde o intuito é carregar um arquivo .txt no padrão CNAB.
        A aplicação foi criada utilizando o framework Odoo, versão 14. Todo o modelo de dados foi criado visando
        atender às especificações do desafio, conforme link abaixo: 
        https://github.com/paulofreire-biz/desafio-dev/blob/main/README.md
    """,

    'author': "Paulo Freire - paulofreire@paulofreire.biz",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'desafio_bycoders',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/loja.xml',
        'views/templates.xml',
        'views/transacao_original.xml',
        'views/transacao.xml',
        'views/tipo_transacao.xml',
        'wizards/importar_arquivo.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
