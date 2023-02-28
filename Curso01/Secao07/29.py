pares = []
impares = []

for i in range(6):
    x = int(input(f'Digite {i+1}: '))
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print('Pares digitados: ', *pares)
print(f'Soma dos pares: {sum(pares)}')
print('Impares digitados: ', *impares)
print(f'Quantidade dos impares: {len(impares)}')