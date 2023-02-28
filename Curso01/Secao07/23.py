vetorA = []
vetorB =[]
escalado = 0

for i in range(5):
    x = float(input(f'Digite numero x{i+1}: '))
    y = float(input(f'Digite numero y{i+1}: '))
    vetorA.append(x)
    vetorB.append(y)
    
    escalado += x*y
print(f'Primeiro vetor:', *vetorA)
print(f'Segundo vetor:', *vetorB)

print(f'Escalado: {escalado}')