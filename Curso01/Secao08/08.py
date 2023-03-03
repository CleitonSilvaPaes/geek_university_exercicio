def hipotenusa(a:float = 0, b:float = 0) -> float:
    return ((a**2) + (b**2))**(1/2)

a = float(input('Digite o cateto A: '))
b = float(input('Digite o cateto B: '))

print(hipotenusa(a, b))