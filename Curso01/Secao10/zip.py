"""
Zip 

Iterar vários iteráveis ​​em paralelo, produzindo tuplas com um item de cada uma.

Exemplo:

>>> for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)

>>> (1, 'sugar')
>>> (2, 'spice')
>>> (3, 'everything nice')

Mais formalmente: retorna um iterador de tuplas, onde a i -ésima tupla contém o i -ésimo elemento de cada um dos argumentos iteráveis.zip()

Outra maneira de pensar é que ele transforma linhas em colunas e colunas em linhas. Isso é semelhante à transposição de uma matriz .zip()

zip()é preguiçoso: os elementos não serão processados ​​até que o iterável seja iterado, por exemplo, por um forloop ou por encapsulamento em um arquivo list.

Uma coisa a considerar é que os iteráveis ​​passados ​​podem ter comprimentos diferentes; às vezes por design e às vezes por causa de um bug no código que preparou esses iteráveis. O Python oferece três abordagens diferentes para lidar com esse problema:zip()

Por padrão, para quando o iterável mais curto é esgotado. Ele irá ignorar os itens restantes nos iteráveis ​​mais longos, cortando o resultado no comprimento do iterável mais curto:zip()


>>> list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
>>> [(0, 'fee'), (1, 'fi'), (2, 'fo')]

zip()é frequentemente usado em casos em que os iteráveis ​​são considerados de comprimento igual. Nesses casos, é recomendável usar a strict=True opção. Sua saída é a mesma que regular :zip()


>>> list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
>>> [('a', 1), ('b', 2), ('c', 3)]

Ao contrário do comportamento padrão, ele gera um ValueErrorse um iterável for esgotado antes dos outros:


>>> for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):  
...     print(item)
 
>>> (0, 'fee')
>>> (1, 'fi')
>>> (2, 'fo')
Traceback (most recent call last):
  ...
ValueError: zip() argument 2 is longer than argument 1

Sem o strict=Trueargumento, qualquer bug que resulte em iteráveis ​​de tamanhos diferentes será silenciado, possivelmente se manifestando como um bug difícil de encontrar em outra parte do programa.

Iteráveis ​​mais curtos podem ser preenchidos com um valor constante para fazer com que todos os iteráveis ​​tenham o mesmo comprimento. Isso é feito por .itertools.zip_longest()

Casos extremos: com um único argumento iterável, retorna um iterador de 1 tupla. Sem argumentos, ele retorna um iterador vazio.zip()

Dicas e truques:

A ordem de avaliação da esquerda para a direita dos iteráveis ​​é garantida. Isso torna possível um idioma para agrupar uma série de dados em grupos de comprimento n usando . Isso repete os mesmos tempos do iterador para que cada tupla de saída tenha o resultado de chamadas para o iterador. Isso tem o efeito de dividir a entrada em blocos de comprimento n.zip(*[iter(s)]*n, strict=True)nn

zip()em conjunto com o *operador pode ser usado para descompactar uma lista:


>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> list(zip(x, y))
>>> [(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zip(x, y))
>>> x == list(x2) and y == list(y2)
>>> True

zip() -> Cria um intevel (Zip Object) que agrega elemento de cada um dos interaveis passados como entreada em pares.
"""

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))