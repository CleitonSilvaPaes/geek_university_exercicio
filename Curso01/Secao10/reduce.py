"""
Reduce

OBS: A partir do Python3+ a funcao reduce() não é mais uma funcao integrada (built-in). Agora temos que importar e utilizar esta funcao a partir do modulo 'functools'

Guido van Rossum: Utilize a funcao reduce() se voce realmente precisa dela. Em todo caso, 99% das vezes um loop for é mais legivel.

Para entender o reduce()

# Imagine que voce tem uma colecao de dados:

dados = [a1, a2, a3, .... an]

# E voce tem uma funcao que recebe dois parametros:

def funcao(x, y):
    return x * y
    
Assim como map() e filter(), a funcao reduce() recebe dois parametros: a funcao e o interal

reduce(funcao, dados)

A funcao reduce(), funciona da seguite forma:
    Passo 1: res1 = f(a1, a2) # Aplica a funcao nos dois primeiros elementos da colecao e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica o funcao passando o resultado do passo1 mais o terceiro elemento e guarda o res.
    
    Isso e repetido ate o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = (resm, an)

Ou seja, em cada passo ela aplica a funcao passando como primeiro argumento o resultado da aplicacao anterio. No final, reduce() ira retornar o resultado final.

Alternativamente, poderiamos ver a funcao reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)

# Como funciona na pratica?

# Vamos utilizar a funcao reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [1,2,3,4,5,6]

# Para utilizar o reduce() nos precisamos de uma funcao que recebe dois paramentos

res = reduce(lambda x, y: x * y, dados)
print(res)
"""

