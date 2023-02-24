soma = 0
for i in range(1001):
    print(i, i % 3 == 0 and i % 5 == 0)
    if i % 3 == 0 and i % 5 == 0:
        soma += i
print(soma)