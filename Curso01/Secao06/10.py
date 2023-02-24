soma = 0
par = 0
num = 0
while par != 51:
    if num % 2 == 0:
        soma += num
        par += 1
    num += 1
print(f'Soma {soma}')