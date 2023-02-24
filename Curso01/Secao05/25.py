a = float(input('Digite o A: '))
b = float(input('Digite o B: '))
c = float(input('Digite o C: '))

delta = (b**2) - (4 * a * c)

x1 = (-(b) + delta**(1/2)) / (2 * a)
x2 = (-(b) - delta**(1/2)) / (2 * a)

if a != 0:
    if delta < 0:
        print('Não exste raiz')
    elif delta == 0:
        print('Raiz unica')
        print(f'X = {x1}')
    elif delta > 0:
        print(f'X1: {x1}')
        print(f'X2: {x2}')


