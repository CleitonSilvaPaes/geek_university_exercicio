chico = 150
ze = 110

rodar = True
count = 0
while rodar:
    count+=1
    ze += 3
    chico+=2

    if ze > chico:
        print(f'Anos: {count}')
        rodar = False