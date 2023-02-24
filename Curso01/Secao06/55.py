num = int(input('Digite: '))
count = 0
soma = 0
if num > 1:
    for i in range(1, num+1):
        for j in range(1, i+1):
            if i % j == 0:
                count+=1
        if count == 2:
            # if not (i in primos):
            soma+= i
        count = 0

print(soma)