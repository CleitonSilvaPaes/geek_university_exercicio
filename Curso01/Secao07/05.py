
pares = []

for i in range(10):
    x = int(input(f'Digite {i+1}°: '))
    if x % 2 == 0:
        pares.append(x)
print(f'Quantidade de pares:{len(pares)} ')
print('Todos os pares digitado: ', *set(pares))