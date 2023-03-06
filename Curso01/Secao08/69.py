def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            if num >= 0:
                valid.append(num)
            else:
                valid.append(None)
        except Exception:
            valid.append(None)
    return valid if None not in valid else None
                    

def denominador_is_zero(d1, d2):
    if d1 > 0 and d2 > 0:
        return True
    return False
    
    
def maximo_divisor(*args):
    n1 , n2 = args
    divisor = max(args)
    for i in range(divisor, 1, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i

def simplificar(*args):
    num, deno, div = args
    return f"""
{num//div}
--
{deno//div}
"""

fracao1 = isint(*input('Digite a fracao 1 a/b: ').split('/'))
fracao2 = isint(*input('Digite a fracao 2 a/b: ').split('/'))

if fracao1 and fracao2 and denominador_is_zero(fracao1[1], fracao2[1]):
    max_div_1 = maximo_divisor(*fracao1)
    max_div_2 = maximo_divisor(*fracao2)
    print(f'Fracao 1 maior divisor comun: {max_div_1}')
    print(f'simplificada: {simplificar(*fracao1, max_div_1)}')
    print(f'Fracao 2 maior divisor comun: {max_div_2}')
    print(f'simplificada: {simplificar(*fracao2, max_div_2)}')
else:
    print('Digite valores valido denominador nao pode ser ZERO')

