s = 0
denominador = 1

for i in range(1, 50+1):
    s += denominador/i
    denominador+=2
print(f'S={s}')