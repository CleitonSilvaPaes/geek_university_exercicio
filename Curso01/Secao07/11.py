negativos = []
positivos = []

for i in range(1, 11):
    x = int(input(f'Digite {i}°: '))
    
    if x < 0 :
        negativos.append(x)
    else:
        positivos.append(x)

print(f'Quantidade de numero negativo: {len(negativos)}. Os numeros:', *negativos)
print(f'Soma dos positivo: {sum(positivos)}')