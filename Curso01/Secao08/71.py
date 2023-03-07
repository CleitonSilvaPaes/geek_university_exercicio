'''
     *                              (10, 10)
     *      *-------------------------*
     *      :                         :
     *      :                         :
     *      :  (1, 5)                 :
     *      :   *                     :
     *      :                         :
     *      :                         :
     *      *-------------------------*
     *   (0, 0)

'''

def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(num)
        except Exception:
            valid.append(None)
    return valid if None not in valid else []
                    

def dentro_ret(*args):
    x, y, v1, v2 = args
    print(args)
    if (x >= v1['x'] and x <= v2['x']) and \
       (y >= v1['y'] and y <= v2['y']):
           return 1
    return 0    

v1 = {'x': 0, 'y': 0}
v2 = {'x': 10, 'y': 10}

x = isint(input('Digite ponto X: '))
y = isint(input('Digite ponto Y: '))

if x and y:
    if dentro_ret(*x, *y, v1, v2):
        print('Dentro do retangulo')
    else:
        print(f'Fora do retangulo')
else:
    print('Digite valores valido')