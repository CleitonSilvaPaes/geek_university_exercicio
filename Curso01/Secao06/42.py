rodar = True
while rodar:
    x = float(input("Digite: "))
    if x <= 0:
        rodar = False
    else:
        print(f'Quadado {x}: {x**2}')
        print(f'Cubo {x}: {x**3}')
        print(f'Raiz {x}: {x**(1/2)}')