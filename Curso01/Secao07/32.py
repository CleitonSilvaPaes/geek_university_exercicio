vet1 = []
vet2 = []

soma = []
produto = []
diferenca = []

for i in range(5):
    x = int(input(f'Digite x{i+1}: '))
    y = int(input(f'Digite y{i+1}: '))
    vet1.append(x)
    vet2.append(y)
    soma.append(x+y)
    produto.append(x*y)
    diferenca.append(x-y)
print(f'Vetor 1: ', *vet1)
print(f'Vetor 2: ', *vet2)
print(f'Soma dos elementos: ', *soma)
print(f'Produto dos elementos: ', *produto)
print(f'Diferenca dos elementos: ', *diferenca)
print(f'Intersecao: ', set(vet1).intersection(vet2))
print(f'Unicao : ', set(vet1).union(vet2))
