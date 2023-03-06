def to_upper(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return chr(ord(char)-32)
    else:
        return('Caracter invalido')

char = input('Digite um caracter de a-z: ')
if len(char) > 1:
    print('Digite somente um caracter')
else:
    print(to_upper(char))