def teste_quadrado(n):
    return (n**(1/2) - int(n**(1/2))) == 0

n = 16

if teste_quadrado(n):
    print(f'{n} é um quadrado perfeito')
else:
    print(f'{n} Nao é um quadrado perfeito')