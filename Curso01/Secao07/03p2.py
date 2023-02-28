matriz = []

for i in range(4):
    arr = []
    for j in range(4):
        arr.append(i*j)
    matriz.append(arr)

for i in matriz:
    print(i)