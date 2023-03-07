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
    return 1

def simplificar(*args):
    num, deno, div = args
    return f"""
{num//div}
--
{deno//div}
"""

def soma_fracao(*args):
    n1, d1, div1, n2, d2, div2 = args
    n1 //= div1
    d1 //= div1
    n2 //= div2
    d2 //= div2
    
    if d1 == d2:
        return f"""
    {n1} {n2:>6}  {n1+n2:>5}
    --  +  --  = --
    {d1} {d2:>6}  {d1:>5}
    """
    
    else:
        return f"""
    {n1} {n2:>6} {(n1*d2) + (d1 * n2):>7}
    --  +  --  =  -- 
    {d1} {d2:>6} {d1*d2:>7}
    """


def subtracao_fracao(*args):
    n1, d1, div1, n2, d2, div2 = args
    n1 //= div1
    d1 //= div1
    n2 //= div2
    d2 //= div2
    
    if d1 == d2:
        return f"""
    {n1} {n2:>6}  {n1-n2:>5}
    --  -  --  = --
    {d1} {d2:>6}  {d1:>5}
    """
    
    else:
        return f"""
    {n1} {n2:>6} {(n1*d2) - (d1 * n2):>7}
    --  -  --  =  -- 
    {d1} {d2:>6} {d1*d2:>7}
    """


def multiplicacao_fracao(*args):
    n1, d1, div1, n2, d2, div2 = args
    n1 //= div1
    d1 //= div1
    n2 //= div2
    d2 //= div2
    
    return f"""
    {n1} {n2:>6} {(n1*n2):>7}
    --  *  --  =  -- 
    {d1} {d2:>6} {d1*d2:>7}
    """
    

def quociente_fracao(*args):
    n1, d1, div1, n2, d2, div2 = args
    n1 //= div1
    d1 //= div1
    n2 //= div2
    d2 //= div2
    
    return f"""
Fracao 1 : {n1//d1}
Fracao 2 : {n2//d2}
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
    print(f'Soma de fracao: {soma_fracao(*fracao1, max_div_1, *fracao2, max_div_2)}')
    print(f'Subtracao de fracao: {subtracao_fracao(*fracao1, max_div_1, *fracao2, max_div_2)}')
    print(f'Multiplicacao de fracao: {multiplicacao_fracao(*fracao1, max_div_1, *fracao2, max_div_2)}')
    print(f'Quociente de fracao: {quociente_fracao(*fracao1, max_div_1, *fracao2, max_div_2)}')
else:
    print('Digite valores valido denominador nao pode ser ZERO')

