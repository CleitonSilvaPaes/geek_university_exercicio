n = int(input('Digite um numero: '))

e = 1

for i in range(1, n+1):
    fatorial = 1
    for j in range(i, 1, -1):
        fatorial = fatorial * j
        # print(fatorial)
    e += 1/fatorial

print(f'E={e}')

