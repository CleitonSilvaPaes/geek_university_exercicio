vet1 = []
soma = []
x = int(input('Digite numero X: '))
y = int(input('Digite numero Y: '))

if (x >=0 and x <= 10000) and (y >= 0 and y <= 10000):
    if x > y:
        x, y = y, x
    for i in range(x, y+1):
        vet1.append(i)
    for i in range(len(vet1)):
        tmp = vet1[i] + vet1[i-1]
        soma.append(tmp)
    print(f'Vetor: ', *vet1)
    print(f'Soma dos algariomos: ', *soma)
else:
    print('Valor Invalido')