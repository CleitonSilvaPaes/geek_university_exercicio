rodando = True
while rodando:
    r1 = float(input('R1: '))
    r2 = float(input('R2: '))

    calc = 0
    
    if calc != 0:
        calc = (r1 * r2)/(r1+r2)
        print(f'R: {calc}')
    else:
        print(f'R: {calc}')
        rodando = False