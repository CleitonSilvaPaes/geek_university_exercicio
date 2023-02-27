s = 0

for i in range(1, 6):
    fatorial = 1
    for j in range(i*2, 1, -1):
        fatorial = fatorial * j
        
    s = s + i/fatorial
print(s)