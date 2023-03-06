def isint(n):
    try:
        num = int(n)
        return num
    except Exception:
        return None

def concatena(str1, str2, num):
    str_res = str2
    for i in range(num):
       str_res += str1[i]
    return str_res+' NULL'

str1 = input('Digite o texto 1: ')
str2 = input('Digite o texto 2: ')
num = isint(input('Digite numero: '))

if num and (num <= len(str1) or num <= len(str2)):
    print(concatena(str1, str2, num))
else:
    print('Digite um tamanho valido')