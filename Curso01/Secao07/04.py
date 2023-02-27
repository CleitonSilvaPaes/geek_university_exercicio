vetor = []
soma = 0

for i in range(8):
    x = int(input(f'Digite {i+1}°: '))
    vetor.append(x)

x = int(input('Digite 1° posicao: '))
y = int(input('Digite 2° posicao: '))

if y < x:
    x, y = y, x

if len(vetor) >= x and len(vetor) >= y:
    for i in range(x, y):
        soma+= vetor[i]

    print(f'Soma entre o intervalo X:{x} e Y:{y} Soma:{soma}')
else:
    print(f'Posicao invalida! ')