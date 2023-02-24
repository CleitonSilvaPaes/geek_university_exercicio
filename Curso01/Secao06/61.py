encontro = False
for i in range(1000, 100, -1):
    for j in range(1000, i, -1):
        mult = i * j
        mult = str(mult)
        if mult == mult[::-1] and not encontro:
            print(f'{i} x {j} = {mult}')
            encontro = True