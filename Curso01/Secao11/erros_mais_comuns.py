"""
Erros mais comuns em Python

ATENCAO: É importante prestar atencao e aprender a ler as saidas de erros geradas peça execucao do nosso codigo.

Os erros mais comuns:

1 - SyntaxError - > Ocorre quando o Python encontra um erro de sintaxe. Ou seja, voce escreveu algo que o Python nao reconhece com parte da linguagem.

a) 
def funcao:
    print('Geey University')

b)
def = 1

c)
return 

2 - NameError -> Ocorre quando uma variavel ou funcao nao foi definida

a)
print(cleiton)

b)
cleiton()

3 - TypeError -> Ocorre quando um funcao/operacao/acao é aplicada a um tipo errado.

a)
print(len(5))

b)
print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos a acessar um elemento  em um lista ou outro tipo de dado indexado utilizando um indice invalido

a)
lista = ['Geek']
print(lista[0][10])

b)
lista = ['Geek']
print(lista[5])

5 - ValueError -> Ocorre quando um funcao ou opercao built-in (indetrada) recebe um argumento com tipo correto mas valor inapropriado.

a)
print(int('Geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionario quando uma chave nao existe

a)
dic = {}
print(dic['geek'])

7 - AttributeError -> Ocorre quando uma variavel nao tem um atributo/funcao

a)
tupla = 12, 2, 31, 4
print(tupla.sort()

8 - IndentationError -> Ocorre quando nao respeitamos a indentacao do Python(4 espaco)

a)
def funcao():
print('Geek')
"""



