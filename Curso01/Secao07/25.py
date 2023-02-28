from random import randrange
vet = []

for i in range(100):
    rodar = True
    while rodar:
        x = randrange(0, 100)
        if x % 7 != 0:
            tmp = str(x)
            tmp = int(tmp[-1])
            if tmp != 7:
                rodar = False
                vet.append(x)

print(*vet)