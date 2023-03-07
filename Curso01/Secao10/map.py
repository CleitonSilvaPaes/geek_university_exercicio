"""
Map

Com map, fazemos mapeamento de valores para funcao

import math 

def area(r):
    '''Calcula a area de um circulo com raio "r".
    
    >>> area(5) # Informando o raio do circulo
    >>> 78.53981633974483 # Resultado da expresao
    '''
    return math.pi * (r ** 2)

Map é uma funcao que recebe dois paranetros: O primeiro a funcao, o segundo um interavel. Retorna um Map Object

raios = [2, 3, 4,5 ,6, 42]
areas = (map(area, raios))
print(list(areas))
>>> [12.566370614359172, 28.274333882308138, 50.26548245743669, 78.53981633974483, 113.09733552923255, 5541.769440932395]

# Usando Expressao Lambdas
import math 

raios = [2, 3, 4,5 ,6, 1]
>>> print(list(map(lambda raio: math.pi * (raio ** 2), raios)))
>>> [12.566370614359172, 28.274333882308138, 50.26548245743669, 78.53981633974483, 113.09733552923255, 3.141592653589793]

OBS: Apos utilizar a funcao map() depos da primeira utilizacao do resultado, ele zera

# Para Fixar - Map
#Temos dados interaveis:
#dados : a1, a2, ..., an

Temos uma Funcao:
# Funcao: f(x)

#Utilizamos a funcao map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a funcao.

# O Map Object: f(a1), f(a2), f(...), f(an) 

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londes', 22)]

# f = 9/5 * c + 32

print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))
>>> [('Berlim', 90), ('Cairo', 104), ('Buenos Aires', 70), ('Los Angeles', 84), ('Tokio', 86), ('Nova York', 88), ('Londes', 76)]

"""