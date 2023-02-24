rodar = True
soma = 0
ultimo = 1
penultimo = 0

LIMITE = 4_000_000

while rodar:
    if soma == 0:
        print(0, 1, end=' ')
    soma = ultimo+penultimo
    penultimo, ultimo = ultimo, soma
    if soma <= LIMITE:
        print(soma, end=' ')
    else:
        rodar = False
    