"""
Utilizando Lambdas

Conhecidas por Expressoes Lambdas, ou simplesmente Lambdas, sao funcoes sem nome, ou seja,
funcao anonimas

# Funcao em Python

def soma(a, b):
    return a + b

print(soma(5, 6))
>>> 11

def funcao(x):
    return 3 * x + 1

print(funcao(3))
>>> 10

# Expressao Lambda
lambda x: 3 * x + 1

# E com utilizar a expressao lambda
calc = lambda x: 3 * x + 1
print(calc(3))
>>> 10

# Podemos ter expressoes lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome : nome.strip().title() + " " + sobrenome.strip().title()
>>> nome_completo('cleiton', 'silva Carvalho Paes')
>>> Cleiton Silva Carvalho Paes


fatorial em Lambda
fat = lambda f: f * fat(f-1) if f > 1 else 1
>>> fat(5)
>>> 120

# Em funcoes Python podemos ter nunhuma ou varia entredas. Em Lambdas tambem

amar = lambda: 'Como nao amar Python?'
uma = lambda x: 3 * x + 1
n = lambda x1, x2, ..., xn: <expressao>

>>> (lambda x, y, z: x + y + z)(1, 2, 3)
6
>>> (lambda x, y, z=3: x + y + z)(1, 2)
6
>>> (lambda x, y, z=3: x + y + z)(1, y=2)
6
>>> (lambda *args: sum(args))(1,2,3)
6
>>> (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
6
>>> (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
6


Ordenando autores pelo sobrenome

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H. G Wells', 'Leigh Brackett']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
>>> ['Douglas Adams', 'Isaac Asimov', 'Leigh Brackett', 'Ray Bradbury', 'Orson Scott Card', 'Arthur C. Clarke', 'Robert Heinlein', 'Frank Herbert', 'H. G Wells']

def gerardora_funcao_quadratica(a, b, c):
    '''Retorna a funcao f(x) = a * x ** 2+ b * x + c'''
    return lambda x: a * x ** 2 + b * x + c
    
gerardora_funcao_quadratica(2, 3, -5)(0)
>>> -5
"""

# Funcao Quadrática
# f(x) = a * x ** 2 + b * x + c

def gerardora_funcao_quadratica(a, b, c):
    """Retorna a funcao f(x) = a * x ** 2+ b * x + c"""
    return lambda x: a * x ** 2 + b * x + c