c = 997
rodar = True
while rodar:
    for b in range(2, 1000-c):
        for a in range(1, b):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                rodar = False
                print(f'{a}+{b}+{c} = {a+b+c}')
                print(f'{a}² + {b}² = {c}²')
    c -=1