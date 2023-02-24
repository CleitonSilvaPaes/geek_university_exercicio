n = int(input('Digite um numero: '))
count = 0

for i in range(1, n+1):
    if i % 11 == 0 \
    and i % 13 == 0 \
    and i % 17 == 0:
        if count == 0:
            print(i)
            count += 1