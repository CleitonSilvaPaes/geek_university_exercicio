rodar = True
soma = 0
count = 0
num = 2
while rodar:
    for i in range(1, num+1):
        for j in range(1, i+1):
            if i % j == 0:
                count+=1
        if count == 2:
            soma+= i
            if soma >= 2_000_000:
                rodar = False
                soma -= i
                break
        count = 0
    num+=1
print(soma)
