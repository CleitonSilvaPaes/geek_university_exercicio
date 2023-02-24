nota = float(input('Digite a nota do aluno: '))
falta = int(input('Digite as Falta do aluno: '))

if nota >= 9 and nota <= 10:
    
    if falta <= 20:
        print('A')
    else:
        print('B')

elif nota >= 7.5 and nota <= 8.9:
    
    if falta <= 20:
        print('B')
    else:
        print('C')

elif nota >= 5.0 and nota <= 7.4:
    
    if falta <= 20:
        print('C')
    else:
        print('D')

elif nota >= 4.0 and nota <= 4.9:
    
    if falta <= 20:
        print('D')
    else:
        print('E')

elif nota >= 0.0 and nota <= 3.9:
    
    if falta <= 20:
        print('E')
    else:
        print('E')