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
    return valid if None not in valid else []
                    

def denominador_is_zero(d1):
    if d1 > 0:
        return True
    return False


def reduz(a, b):
    return f"""
Representacao de numeros Racionais
{a:>2}
---
{b:>2}
"""


def neg(*args):
    a, b = args
    return f"""
Negacao de racionais
{-a:>9}
{-a} = - ---
{1:>9}
{-b:>9}
{-b} = - ---
{1:>9}
"""


def soma(*args):
    a, b = args
    return f"""
Soma de racionais
{a:>2} {b:>7} {a+b:>7}
---  +  ---  =  ---
{1:>2} {1:>7} {1:>7}
"""

def mult(*args):
    a, b = args
    return f"""
Multiplicacao de racionais
{a:>2} {b:>7} {a*b:>7}
---  *  ---  =  ---
{1:>2} {1:>7} {1:>7}
"""


def div(*args):
    a, b = args
    return f"""
Divisao de racionais
{a:>2} {b:>7} {a:>7} {1:>7} {a:>7}
---  /  ---  =  ---  *  ---  =  ---  =  {a/b:.2f}
{1:>2} {1:>7} {1:>7} {b:>7} {b:>7}
"""


a = isint(input('Digite um numero positivo: '))
b = isint(input('Digite um numero positivo: '))

if a and b and denominador_is_zero(*b):
    print(reduz(*a,*b))
    print(neg(*a, *b))
    print(soma(*a, *b))
    print(mult(*a, *b))
    print(div(*a, *b))
    
else:
    print('Digite valores valido!')