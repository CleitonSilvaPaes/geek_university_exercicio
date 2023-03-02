numeros = int(input('Digite um valor: '))

def calcular(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return int(calcular(n - 1, k - 1)) + int(calcular(n - 1, k))

for i in range(numeros):
    pascal = []
    for j in range(i+1):
        pascal.append(calcular(i, j))
    print(*pascal)