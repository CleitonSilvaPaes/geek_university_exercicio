soma = 0 

for i in range(1, 11):
    x = int(input(f'Digite um numero {i}°: '))

    if x >= 0 :
        soma += x

media = soma/10

print(f'Media dos numeros: {media}')