"""
PEP 8 - Python Enhancement Proposal

Sao proposta de melhorias para linguagem Python

The Zem of Python, by Tim Peters.

import this

A ideia do PEP8 e que possamos escrever codigos Python de forma Pythonica.

[1] - Utilize Camel Case para nomes de classes;

[2] - Depos de uma declaracao deixar duas linhas em brancos;
    - Separacao de funcao e definicao de classe;
    - Metodos dentro de uma classe devem ser separados com uma única linha em branco

[3] - Utilize nomes em minusculo, separados por underline para funcao ou variavel;

[4] - Utilize 4 espacos para indentacao! (Nao use TAB)

[5] - Imports 
    - Imports devem ser sempre feitos em linhas separadas;

    # Imports Errado
    import sys, os

    # Imports Certo
    import sys
    import os

    # Nao ha problema em utilizar:
    from types import StringType, ListType # Pois os dois sao do mensmo pacote

    # Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

    from types import (
        StringType,
        ListType,
        SetType,
        OutroType
    )

    # Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou doctrings e antes de constantes ou variaveis globais.

[6] - Espacos em expressoes e instrucoes
    # Nao faca:

    funcao([ algo[1], { outro : 2} ] )

    # Faca:
    funcao([algo[1], {outro: 2}])

    # Nao Faca
    x              = 1
    y              = 2
    variavel_longa = 5

    # Faca:
    x = 1
    y = 2
    variavel_longa = 5

[7] - Termine sempre uma instrucao com uma nova linha
"""

class Calculadora: # Camel Case
    pass


class CalculadoraCientifica: # Quado tem nome composto colocar sempre as inicial Maiuscula
    pass


def mostrar_na_tela(): # Uma funcao no pep8 
    pass

