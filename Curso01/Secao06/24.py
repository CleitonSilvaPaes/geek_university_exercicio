n = int(input('Digite um numero: '))
soma = 0
for i in range(1, n):
    if n % i == 0:
        soma += i

print(soma)