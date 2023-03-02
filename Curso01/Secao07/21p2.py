import os
from random import random, seed

seed(1)

n_linhas, n_coluna = 2, 2

# Matriz original 1
matriz1 = [[round(random() * 10, 0) for i in range(n_coluna)]for j in range(n_linhas)]
# Matriz original 2
matriz2 = [[round(random() * 10, 0) for i in range(n_coluna)]for j in range(n_linhas)]

# Funcao para calcular soma ou subtracao
def operacao_matriz(matriz1:list, matriz2:list, opcao:str):
    resultado = []
    for i in range(len(matriz1)):
        arr = []
        for j in range(len(matriz1[i])):
            print(opcao)
            if opcao == 'a':
               calc = matriz1[i][j] + matriz2[i][j]
            else:
                calc = matriz1[i][j] - matriz2[i][j]
            arr.append(calc)
        resultado.append(arr)
        
    print(f'Resultado')
    opcao = ' - ' if opcao == 'b' else ' + '
    for i in range(len(resultado)):
        print(matriz1[i], opcao, matriz2[i], ' = ', resultado[i])

rodar = True
while rodar:
    print("""
   Escolha as Opcao para finaliza o programa

(a) - somar as duas matriz
(b) - subtrair a primeira matriz da segunda
(c) - adicionar uma constante as duas matriz 
          """)
    opcao = input('Digite a opcao desejada: ').lower()
   
    if opcao == 'a':
        rodar = False
        operacao_matriz(matriz1, matriz2, opcao)
                
    elif opcao == 'b':
        rodar = False
        operacao_matriz(matriz1, matriz2, opcao)

    elif opcao == 'c':
        rodar = False
        
        linha = int(input('Digite a linha: '))-1
        coluna = int(input('Digite a coluna: '))-1
        
        if (linha >= 0 and linha <= len(matriz1)-1) and (coluna >= 0 and coluna <= len(matriz1)-1):
            valor = float(input('Digite o valor: '))
            
            print('Matrizs original')
            for i in range(len(matriz1)):
                print(matriz1[i], ' | ', matriz2[i])
            
            matriz1[linha][coluna] = valor
            matriz2[linha][coluna] = valor
            
            print(f'Resultado')
            for i in range(len(matriz1)):
                print(matriz1[i], ' | ', matriz2[i])
            
        else:
            print('Linha ou a coluna informada invalido')