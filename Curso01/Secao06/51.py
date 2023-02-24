ANO_ATUAL = 2000
CONTRATADO = 1995
persentual = 0.015
salario = 2000
for i in range(CONTRATADO, ANO_ATUAL+1):
    salario = salario + (salario * persentual)
    persentual *= 2
    print(salario)