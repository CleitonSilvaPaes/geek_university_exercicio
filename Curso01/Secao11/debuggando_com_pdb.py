"""
Debuggando com PDB

PDB - Python Debugger

Vida de inseto -> Life's Bug

Bug -> Inseto

# OBS: A utilizacao do print() para debugar codigo e uma pratica ruim.

def dividir(a, b):
    print(f'a={a}, b={b})
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}

print(dividir(4, 7))
>>> a=4, b=7
>>> 0.5714285714285714

# Exemplo com PDB - Python Debugger

# Para utilzizar o Python Debugger, precisamos* importar oa biblioteca pdb e entao utilizar a funcao set_trace()

# Comandos basicos do PDB
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime varical)
# c (continua a execucao - finaliza o debugger)

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Python programacao'
final = nome_completo + ' faz o curso ' + curso

# Porque utilizar esse formato?
# O debug é utilizado durante o desenvolvimento. Custumamos realizar todos os import de bibliotecas no inicio do arquivo. Por isso, ao inves de colocarmos o import do pdb no inicio do arquivo, nos colocamos somente onde camos debugar, e ao finalizar ja fazemos a remocao

# OBS: Cuidado com conflitos entre nomes de variaveis e os comandos do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1,2,3,4))

# Como os nomes das variavels sao os mesmos dos comandos do pdb, devemos utilizar o comando p para imprimir as variaveis. Ou seja: p nome_da_variavel

# Nada de colocar nomes nao representativos em variaveis. Sempre optar por nomes significativos.
"""




