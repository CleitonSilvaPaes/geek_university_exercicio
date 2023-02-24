rodar = True
n = int(input('Digite: '))
soma = 0
ultimo = 1
penultimo = 0
while rodar:
    if soma == 0:
        print(0, 1, end=' ')
    soma = ultimo+penultimo
    print(soma, end=' ')
    penultimo, ultimo = ultimo, soma
    if soma > n:
        rodar=False
    