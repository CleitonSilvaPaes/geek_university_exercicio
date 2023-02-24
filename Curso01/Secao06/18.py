n = int(input('Digite um numero: '))
maior = 0
vezes = 0
for i in range(n):
    x = int(input('Digite um valor: '))
    if i == 0:
        maior = x
        vezes += 1
    elif maior == x:
        vezes +=1
    elif maior < x:
        maior = x
        vezes = 1

print(f'Maior digitado {maior} -- Vezes: {vezes}')
