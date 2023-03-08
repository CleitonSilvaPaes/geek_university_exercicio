"""
O bloco try/except

Utilizamos o bloco try/except para tratar error que podem ocorrer no nosso codigo. Previnindo assim que o programa pare de funcionar e o funcionar e o usuario receba mensagens de erro inesperadas.

try:
    # execucao problematica
except:
    # O que deve ser feito em caso de problema


# Exemplo 1 - Tratando um erro generico

try:
    geek()
except Exception as e:
    print('Ocorreu um problema')
    
# Tente executar a funcao geek(), caso voce encontre erros, imprima a mensagem de erro 

# Exemplo 2 - Tratando um erro generico

try:
    len(5)
except Exception as e:
    print('Ocorreu um problema')
    
# Tente executar a funcao geek(), caso voce encontre erros, imprima a mensagem de erro

OBS: Tratar erro de forma generica nao e a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma especifica.

# Exemplo 3 - Tratando um erro forma espefica

try:
    geek()
except NameError:
    print('Voce esta utilizando uma funcao inexistente')
    
# Exemplo 4 - Tratando um erro forma espefica

try:
    len(5)
except NameError:
    print('Voce esta utilizando uma funcao inexistente')
except TypeError:
    print('Tipo de dado invalido')
"""


