from io import StringIO
from random import randint

def bit_length(num):
    s = bin(num)
    s = s.lstrip('0b')
    return s


vetor = [randint(1, 1000) for i in range(10)]

with StringIO('') as arq:
    for i in vetor:
        binario = bit_length(i)
        arq.write(binario)
        arq.write('\n')
    arq.seek(0)
    print(arq.read())