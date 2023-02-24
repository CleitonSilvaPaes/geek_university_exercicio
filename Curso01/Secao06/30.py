n = int(input('Digite um numero: '))

sequencia1 = 0
sequencia2 = 0
sequencia3 = 0

for i in range(1, n+1):
    sequencia1 += i
print(f'Sequencia 1: {sequencia1}')

inverte = False
for i in range(1, (n*2-1)):
    if not inverte:
        sequencia2 += i
        inverte = True
    else:
        sequencia2 -= i
        inverte = False
print(f'Sequencia 2: {sequencia2}')

for i in range(1, (2*n-1)):
    if i % 2 != 0:
        sequencia3 += i

print(f'Sequencia 3: {sequencia3}')
