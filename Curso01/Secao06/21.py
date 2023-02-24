x = int(input('Digite um numero 1: '))
y = int(input('Digite um numero 2: '))

soma = 0
mult = 1

for i in range(x, y+1):
    if i % 2 == 0:
        soma += i
    else:
        mult *= i

print(f'Soma : {soma} -- Multiplicacao: {mult}')