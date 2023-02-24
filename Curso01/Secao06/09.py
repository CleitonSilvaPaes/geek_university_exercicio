n = int(input('Digite um numero: '))

for i in range(n+1):
    if i % 2 != 0:
        print(f'{i}', end=' ')