"""
Try / Except / Else / Finally

Dica de quando e onde tratar codigo:

TODA ENTRADA DEVE SER TRATADA!

OBS: A funcao do usuario e DESTRUIR seu sistema

try:
    num = int(input('Digite um numero: '))
except ValueError as err:
    print(f'Voce digitou letra mas tem que digitar numero')
else:
    print(f'Voce digitou {num}')
    
# Finally
try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Voce nao digitou um valor valido. ')
else:
    print(f'Voce digitou o numero {num}')
finally:
    print('Executando o finally')
    
# OBS: O bloco finally é SEMPRE executado. Indenpendente se houve excecao ou nao.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADO

def div(a, b):
    return a / b


num1 = int(input('Digite o primeiro numero: '))
try:
    num2 = int(input('Digite o segundo numero: '))
except ValueError:
    print('O valor precisa ser numerico')

try:
    print(div(num1, num2))
except NameError:
    print('Valor Incorreto')


# Exemplo mais complexo CORRETO

def div(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valores incorreto'
    except ZeroDivisionError:
        return 'Nao é possivel realizar uma divisao por zero'
    
a = input('Digite numero 1°: ')
b = input('Digite numero 2°: ')

print(div(a, b))
"""

# Exemplo mais complexo CORRETO

def div(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valores incorreto'
    except ZeroDivisionError:
        return 'Nao é possivel realizar uma divisao por zero'
    
a = input('Digite numero 1°: ')
b = input('Digite numero 2°: ')

print(div(a, b))