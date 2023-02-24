n = int(input('Digite um numero: '))

e = 1

for i in range(1, n+1):
    e += 1/i**i

print(f'E={e}')