def compara(str1, str2):
    return str1 == str2

str1 = input('Digite o texto 1: ')
str2 = input('Digite o texto 2: ')

if compara(str1, str2):
    print('Os dois texto sao iguais')
else:
    print('Nao sao iguais')