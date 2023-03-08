"""
Leitura de Arquivos

Para ler o conteudo de um arquivo em Python, utilizamos a funcao integrada
open().

open() -> Na forma mais simples de utilizacao nos passamos apenas um parametro de entreda, qye neste caso e o caminho para o arquivo a ser lido. Essa funcao retorna um _io.TextIOWrapper e com ele que trabalhamos

https://docs.python.org/3/library/functions.html#open

OBS: Por padrao, a funcao open() abre o arquivo para leitura. Esse arquivo deve existir, ou entrao teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode ='r' -> Modo de leitura. r -> read() -> str

"""

# Exemplo
arquivo = open("texto.txt", encoding='utf-8')

print(arquivo.read())

# Para ler o conteudo de um arquivo, apos sua abertura, devemos utilizar a funcao read()

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor quando estamos escrevendo.

# OBS: A funcao read() le todo o conteudo do arquivo

#read file python?