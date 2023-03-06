def intercalacao(str1, str2):
    string = str()
    for i in range(len(str1)):
        string += ''.join(str1[i])
        string += ''.join(str2[i])
        string += ' '
    return string


str1 = input('Digite o texto 1: ')
str2 = input('Digite o texto 2: ')

if len(str1) == len(str2):
    print(intercalacao(str1, str2))
else:
    print('Os dois texto tem que ter o mesmo tamanho!')