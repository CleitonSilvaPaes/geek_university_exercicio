lista = []
for i in range(6):
    x = int(input(f'Digite {i+1}°: '))
    lista.append(x)

print(f'Valores lido: ', *lista)