from random import randrange

vet = [[randrange(30) for i in range(4)] for j in range(4)]

count = 0

for i in vet:
    for j in i:
        if j > 10:
            count+=1

print(vet)
print(f'Posui: {count}')