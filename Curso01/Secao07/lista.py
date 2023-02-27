"""
Listas 

Listas em Python funcional com vetores/matrizes (arrays) elas sao dinamicas de tamanho tambem de valores

Dinamico: Nao possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos

- Quaquer tipo de dado: Nao possuem tipo de dado fixo; Ou seja, podemos colocar string, int, bool, float, list, dict.

As lista em Python sao representadas por conchetes: []

append: Adiciona um unico valor na lista no final 

extend: Adiciona um consuto de valores na lista, nao aceita um unico valor
somente interaveis e ao final da lista

sort: Ordena do menor para o menor

insert: Adiciona um elemento na lista mas na posicao desejada e nao subtitui o valor inicial o memmo será deslocado para direira.

+: atribuicao de lista o mesmo que extend

copy: Funcao que copia a lista para nao perder os dados da anterior

len: Mostra a quantidade de elementos da lista

pop: remove o ultimo elemento da lista e retorna o mesmo ou remover com o index
do elemento desejado exemplo:
    lista = [2,3,4,5,6]
    lista.pop()
    retorno 6 -- [2,3,4,5]
              ou
    lista.pop(2)
    retorno 3 -- [2,4,5]

clear: remove todos os elementos.

*: repete elementos da lista exemplo:
    lista = [1,2,3]
    nova = lista * 2
    nova = [1,2,3,1,2,3]

split: Separa elementos e transforma em uma lista exemplo:
    valor = 'Cleiton Silva'.split()
    valor = ['Cleiton', 'Silva']

join(): Junta elemento de uma lista exemplo: 
    valor = ['Cleiton', 'Silva']
    nome = ' '.join(valor)
    nome = 'Cleiton Silva'

slicing
lista [inicio:fim:passo]

lista = [1,2,3,4]

lista[1:] -- [2,3,4]

lista[:2] -- [1,2] = 2-1 = 0, 1

lista[:4] -- [1,2,3,4] = 4-1 = 0 ,1, 2, 3

lista[1:3] = comecao em 1, pega ate indece 3 = 3-1 [2,3] não inclui o elemento 3 que seria 4
"""

