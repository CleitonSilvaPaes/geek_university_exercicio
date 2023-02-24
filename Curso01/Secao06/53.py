n = int(input('Digite um valor: '))
num = 0
for i in range(n):
    for j in range(i+1):
        num+=1
        print(num, end=' ')
    print()