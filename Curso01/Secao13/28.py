from io import StringIO


arq_init = StringIO("""Hoje é dia de prova de AP
A prova está muito fácil
Vou tirar uma boa nota
""")

file = [i[::-1] for i in arq_init.readlines()[::-1]]

with StringIO('') as arq_final:
    for i in file:
        arq_final.write(i)
    arq_final.seek(0)
    print(arq_final.read())
    
arq_init.close()