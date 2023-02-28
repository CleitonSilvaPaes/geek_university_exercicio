from random import randrange

vet = [[randrange(10) for i in range(5)] for j in range(5)]

print(f'Matriz Original: ')
for i in vet:
    print(i)

for i in range(len(vet)):
    for j in range(len(vet[i])):
        if i == j:
            vet[i][j] = 1
        else:
            vet[i][j] = 0

print(f'Matriz : ')
for i in vet:
    print(i)