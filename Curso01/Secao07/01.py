vetor = [1, 0, 5, -2, -5, 7]
soma = 0 
for i in range(len(vetor)-3):
    soma += vetor[i]
print(soma)
vetor[4] = 100
print(vetor)