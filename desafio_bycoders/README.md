# Importação de arquivo .txt no padrão CNAB

Trata-de um desafio criado pela empresa bycoders_ onde o intuito é carregar um arquivo .txt no padrão CNAB.
A aplicação foi criada utilizando o framework Odoo, versão 14. Todo o modelo de dados foi criado visando
atender às [especificações do desafio.](https://github.com/paulofreire-biz/desafio-dev/blob/main/README.md)

# Instruções para instalação
Por tratar-se de uma aplicação Odoo, versão 14, Community version, a instalação da aplicação segue o mesmo padrão de 
qualquer aplicação Odoo. Ou seja, basta copiar todos os arquivos e diretórios que estão abaixo de desafio_bycoders para seu diretório de 
aplicações Odoo. Depois é só ir na opção "Aplicativos" e pesquisar pela aplicação "desafio_bycoders" e clicar em instalar.

# Navegação pela aplicação
Ao efetuar login como administrador e selecionar a aplicação Desafio bycoders_, será exibida como padrão as transações já carregadas e processadas.
Porém, na primeira vez, nenhum registro estará disponível. Para efetuar a carga inicial, clicar na opção "Importar Arquivo". Uma vez que o arquivo é selecionado e 
clicado no botão "Importar", os registros do arquivo .txt serão processados sequencialmente. Agora já é possível navegar pelos menus e desfrutar dos dados existentes.

# Telas da aplicação
É possível visualizar [algumas telas da aplicação](https://github.com/paulofreire-biz/desafio-dev/tree/main/telas-odoo) 

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

```diff
Obs.: Achei estranho o tipo de transação "débito" ser considerada com Entrada, porém segui a definição do enunciado.
```

# Agrupamento das transações
Na opção Transação, ao clicar no botão "Agrupado por", é possível agrupar as transações de duas formas:
1. Por Loja
2. Por Tipo de Transação

# Outras funcionalidades
Apesentamos no menu Configuração, os Tipos de Transações, assim como as Transações Originais (aquelas descritas no passo 1 da sequência de processamento)

# Testes automatizados
Foram criados os seguintes testes automatizados: test_inserir_transacao_original, test_inserir_transacao e test_inserir_tipo_transacao.

Não cheguei a criar testes para a UI de upload de arquivos por falta de tempo e conhecimento. 

# Docker compose
Não domino tal tecnologia, porém dei uma breve pesquisada no assunto. No caso das minhas aplicações Odoo, costumo fazer deploy
sempre via GitHub e costuma ser algo prático, fácil e seguro. Mas gostaria de conhecer mais sobre o Docker.

#Comentários Pessoais
Aproveitei este desafio para me aprofundar um pouco mais no framework Odoo. Agrdeço pela oportunidade!