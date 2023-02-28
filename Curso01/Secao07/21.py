vetorA = []
vetorB = []
vetorC = []

for i in range(1, 11):
    x = float(input(f'Digite vetor A {i}: '))
    y = float(input(f'Digite vetor B {i}: '))
    vetorA.append(x)
    vetorB.append(y)
    vetorC.append(x-y)

print(*vetorC)