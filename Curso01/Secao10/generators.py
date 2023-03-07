"""
Generators Expression

Em aulas anteriores nos estudamos:
    - List Comprehension;
    - Dictionaty Comprehension;
    - Set Comprehension;
    
Nao vimos:
    - Tuple Comprehension ... porque elas se chanan Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))
>>> True

# Poderiamos ter feito utilizando Generators
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))


# Qual é a utilidade getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parametro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' esta ocupando em memoria. Quanto maior a string, mais espaco ocupa.
print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(5646545466584))
print(getsizeof(True))

--------------------------------------------------------------------------------

from sys import getsizeof

# Gerando uma lista de numeros com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando um lista de numeros com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando um lista de numeros com Dictionary Comprehension
dict_comp = getsizeof({x:x * 10 for x in range(1000)})

# Gerando um lista de numeros Generators
gen = getsizeof((x * 10 for x in range(1000)))

print('Para fazer a mesma tarefa gastamos em memoria: ')
print(f'List Comprehension: {list_comp} bytes')
>>> 8856 bytes
print(f'Set Comprehension: {set_comp} bytes')
>>> 32984 bytes
print(f'Dictionary Comprehension: {dict_comp} bytes')
>>> 36960 bytes
print(f'Generators Expression: {gen} bytes')
>>> 112 bytes

"""

# Eu posso iterar no Genarator Expression? Sim!
from sys import getsizeof

gen = (x * 10 for x in range(1000))
for num in gen:
    print(num)