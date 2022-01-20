# Importação de arquivo .txt no padrão CNAB

Trata-de um desafio criado pela empresa bycoders_ onde o intuito é carregar um arquivo .txt no padrão CNAB.
A aplicação foi criada utilizando o framework Odoo, versão 14. 

# Instruções para instalação
Por tratar-se de uma aplicação Odoo, versão 14, Community version, as instruções de instalação se fazem desnecessário.

# Navegação pela aplicação
Ao efetuar login como administrador e selecionar a aplicação Desafio bycoders_, será exibida como padrão as transações já carregadas e processadas.
Na primeira, porém nenhum registro estará disponível. Para efetuar a carga inicial, clicar na opção "Importar Arquivo". Uma vez que o arquivo for selecionado e 
clicado no botão "Importar", os registros do arquivo .txt serão processados sequencialmente.

# Processamento dos registros do arquivo .txt
**Sequência de processamento:**

1. São carregados os registros do arquivo .txt para um modelo intermediário que chamamos de desafiobc.transacao.original
2. Os tipos de transações são populados no modelo desafiobc.tipo.transacao, uma vez que o mesmo será utilizado no passo seguinte
3. São carregados os registros agora no modelo definitivo chamado desafiobc.transacao.

Obs: cada processamento acima apenas irá ocorrer na primeira vez, para repetir a execução é necessária a limpeza das tabelas 
respeitando a ordem das foreign keys.

# Saldo por loja
Para consultar o saldo de cada loja, basta ir no menu Configuração / Loja. Ao clicar na respectiva loja, será possível visualizar
as transações, bem como os donos de cada loja. 

# Agrupamento das transações
Na opção Transação, ao clicar no botão "Agrupado por", é possível agrupar as transações por Loja e Tipo de Transação. 

# Outras funcionalidades
Apesentamos no menu Configuração, os Tipos de Transações, assim como as Transações Originais (aquelas descritas no passo 1 da sequência de processamento)

# Testes automatizados
Foram criados os seguintes testes automatizados: test_inserir_transacao_original, test_inserir_transacao e test_inserir_tipo_transacao.

Não cheguei a criar testes para a UI de upload de arquivos por falta de tempo e conhecimento. 

# Docker compose
Não domino tal tecnologia, porém dei uma breve pesquisada no assunto. No meu caso costumo fazer deploy de aplicações via Git.

#Comentários Pessoais
Aproveitei este desafio para me aprofundar um pouco mais no Odoo. Obrigado pela oportunidade!