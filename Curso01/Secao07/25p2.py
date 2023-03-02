import os
from random import choice
from time import sleep

jogador = 1

# Monta o tabuleiro
tabuleiro = [[0 for i in range(3)] for j in range(3)]

rodar = True
while rodar:
    # Pegar todas as posivel movimento
    possiblildidade = []
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] == 0:
                possiblildidade.append((i, j))
                
    if jogador == 1:
        rodar2 = True
        while rodar2:
            print('Tabuleiro')
            for i in tabuleiro:
                print(i)
            linha = int(input('Digite a linha: '))-1
            coluna = int(input('Digite a coluna: '))-1
            
            if linha >= 0 and linha <= len(tabuleiro) and coluna >= 0 and len(tabuleiro[0]):
                if tabuleiro[linha][coluna] == 0:
                    tabuleiro[linha][coluna] = jogador
                    rodar2 = False
                else:
                    os.system('cls')
                    print('Posicao invalida')
                    sleep(1)
            else:
                os.system('cls')
                print('Cordenada invalida')
                sleep(1)
    else:
        os.system('cls')
        x, y = choice(possiblildidade)
        tabuleiro[x][y] = jogador
        
    diagonal_p = 0
    diagonal_i = 0
    for i in range(len(tabuleiro)):
        diagonal_p += tabuleiro[i][i]
        diagonal_i += tabuleiro[i][i-1-i]
    if (diagonal_p == 3 or diagonal_p == 3) \
        or (diagonal_i == 3 or diagonal_i == -3):
            rodar = False
            os.system('cls')
            print(f'Parabens Jogador {jogador}')
            print()
            print('Tabuleiro')
            for i in tabuleiro:
                print(i)
    else:
        for i in range(len(tabuleiro)):
            soma_h = 0
            soma_v = 0
            for j in range(len(tabuleiro[i])):
                soma_h += tabuleiro[i][j]
                soma_v += tabuleiro[j][i]
            if (soma_h == 3 or soma_h == -3) or \
                (soma_v == 3 or soma_v == -3):
                    rodar = False
                    os.system('cls')
                    print(f'Parabens Jogador {jogador}')
                    print()
                    print('Tabuleiro')
                    for i in tabuleiro:
                        print(i)
                    
    jogador *= -1