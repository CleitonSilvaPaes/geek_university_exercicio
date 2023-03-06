def isint(n):
    try:
        n = int(n)
        if n > 0:
            return n
        return None
    except Exception:
        return None


def rotina(tam):
    string = str()
    rodar = True
    while rodar:
        if len(string) < tam:
            char = input('Digite um character: ')
            if char == '':
                rodar = False
            elif len(char) == 1:
                string += ''.join(char[0])
            else:
                print('Digite somente uma letra')
        else:
            rodar = False
       
    return string


num = isint(input('Digite o tamanho da string: '))
if num:
    print(rotina(num))
else:
    print('Digite um valor valido!')