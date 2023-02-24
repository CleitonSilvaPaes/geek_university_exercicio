x = int(input('Digite 1°: '))
y = int(input('Digite 2°: '))

soma = 0

if y > x:
    for i in range(x, y+1):
        if i % 2 != 0:
            soma += i
    print(f'Soma dos impares nesse intervalo: {soma}')
else:
    print('Digite um intervalo valido: ')
