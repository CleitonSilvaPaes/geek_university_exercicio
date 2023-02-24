n = int(input('Digite um numero: '))
if n % 2 != 0:
    for i in range(n, -1, -1):
        if i % 2 != 0:
            print(i, end=' ')
else:
    print('Numero não é impar')