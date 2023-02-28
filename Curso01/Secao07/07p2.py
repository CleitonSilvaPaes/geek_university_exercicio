n = 10

matriz = []

for i in range(n):
    arr = []
    for j in range(n):
        if i < j:
            calc = (2*i) + (7*j-2)
        elif i == j:
            calc = (3*(i**2)) - 1
        else:
            calc = (4*(i**3)) - (5*(j**2)) + 1
        arr.append(calc)
    matriz.append(arr)

for i in matriz:
    print(i)