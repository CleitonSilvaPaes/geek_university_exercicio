rodar = True

num = 0
count = 0

while rodar:
    num+=1
    count = 0
    for i in range(1, 11):
        if num % i == 0:
            count += 1
            if count == 10:
                rodar = False
    
print(num)