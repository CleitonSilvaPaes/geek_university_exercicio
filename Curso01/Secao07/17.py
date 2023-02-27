vetor = []

for i in range(1, 11):
    x = float(input(f'Digite {i}: '))
    if x < 0:
        vetor.append(0)
    else:
        vetor.append(x)

print(*vetor)