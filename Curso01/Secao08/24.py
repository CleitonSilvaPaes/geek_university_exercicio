def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []

def pilha(*args):
    n = args[0]
    m = (2 * n) - 2  
    for i in range(0, n):  
        for j in range(0, m):  
            print(end=" ")  
        m = m - 1  
        for j in range(0, i + 1):    
            print("*", end=' ')  
        print()  

num = input('Digite um numero Inteiro: ')
num = isint(num)
if num:
    pilha(*num)
else:
    print('Digite um numero')
    