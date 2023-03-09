"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrao
w -> Abre para escrita - sobrescreve caso o arquivo ja exista

https://docs.python.org/3/library/functions.html#open

--------------------------------------------------------------------------
| Caracter | Significado                                                 |
|------------------------------------------------------------------------|
|    'r'   | aberto para leitura (padrao)                                |
|------------------------------------------------------------------------|
|    'w'   | aberto para gravacao, truncando o arquivo primeiro          |
|------------------------------------------------------------------------|
|    'x'   | criacao exclusiva, falhando se o arquivo ja existir         |
|------------------------------------------------------------------------|
|    'a'   | aberto para escrita, anexando ao final do arquivo se existir|
|------------------------------------------------------------------------|
|    'b'   | modo binario                                                |
|------------------------------------------------------------------------|
|    't'   | modo de texto(padrao)                                       |
|------------------------------------------------------------------------|
|    '+'   | aberto para atualizacao (leitura e escrita)                 |
--------------------------------------------------------------------------

O modo padrão é 'r'(aberto para leitura de texto, sinônimo de 'rt'). Modes 'w+'e 'w+b'abrir e truncar o arquivo. Modes 'r+' e 'r+b'abra o arquivo sem truncamento.

Conforme mencionado em Visão geral , o Python distingue entre E/S de texto e binário. Arquivos abertos em modo binário (inclusive 'b'no argumento mode ) retornam conteúdos como bytesobjetos sem nenhuma decodificação. No modo de texto (o padrão, ou quando 't'está incluído no argumento mode ), o conteúdo do arquivo é retornado como str, os bytes tendo sido primeiro decodificados usando uma codificação dependente de plataforma ou usando a codificação especificada , se fornecida.
"""