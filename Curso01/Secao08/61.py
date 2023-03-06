from random import randint

def anagrama(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    print(s1,s2)
    if s1 == s2:
        return True
    return False

s1 = input('Digite o texto 1: ')
s2 = input('Digite o texto 2: ')

if anagrama(s1, s2):
    print('Texto digitado anagrama')
else:
    print('Infelimente nao anagrama')