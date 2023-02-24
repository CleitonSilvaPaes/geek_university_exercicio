rodar = True
soma = 0
qtd = 0
media = 0
maior = 0
menor = 0
pares = 0
count = 0

while rodar:
    x = int(input('Digite numero: '))
    soma += x
    qtd += 1
    if x != 0:
        if qtd == 1:
            maior, menor = x,x
        elif maior < x:
            maior = x
        elif menor > x:
            menor = x
        if x % 2 == 0:
            pares += x
            count += 1
    else:
        rodar = False

print(f'Soma dos numeros digitados: {soma}')
print(f'A quantidade de numeros digitados: {qtd}')
print(f'Media dos numeros digitados: {soma/qtd}')
print(f'Maior numero digitado: {maior}')
print(f'Menor numero digitado: {menor}')
print(f'Media dos numeros pares: {pares/count}')