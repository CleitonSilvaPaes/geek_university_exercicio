menor = 0
maior = 0
for i in range(1, 11):
    x = int(input(f'Digite {i}°: '))
    if i == 1:
        maior, menor = x, x
    elif maior < x:
        maior = x
    if menor > x:
        menor = x
print(maior, menor)