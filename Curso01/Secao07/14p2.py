
from random import randrange

n = 5

bingo = []

# Monta a cartela
for i in range(n):
    arr = []
    for j in range(n):
        rodar = True
        while rodar:
            num = randrange(1, 99)
            if len(bingo) == 0:  # Adiciona o primeiro array
                if num not in arr:
                    arr.append(num)
                    rodar = False
            else:  # Verifica se tem no array
                encontrou = 0
                for linha in range(len(bingo)):
                    if num in bingo[linha]:
                        encontrou += 1
                if encontrou == 0 and len(arr) < 5:
                    arr.append(num)
                    rodar = False
    bingo.append(arr)

print('Cartela do bingo:')
for i in bingo:
    print(i)
