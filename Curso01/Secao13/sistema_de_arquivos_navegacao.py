"""
Sistema de Arquivos e Navegaçao

Para fazer uso de manipulacao de arquivos do sistema de operacional, precisamos importar e fazer uso do modulo os.

os -> Operating System - Sistema Operacional

# getcwd() -> pega o current work directory - diretorio de trabalho corrente
# Retorna o path (caminho absoluto)
print(os.getcwd())

# Para mudar de o diretorio, podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd())

# Podemos checar se um diretorio e absoluto ou relativo

print(os.path.isabs('/Curso/Curso1/'))

# OBS para usuarip Windows
# Se voce, infelizmente, estivar utiliznado um computador com windows.
# Tera que ter cuidado ao verificar diretorios.
print(os.path.isabs('C:\\Curso\\Curso1\\'))

# Podemos identificar o sistema operacional com o mofulo os
print(os.name) # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhe no sistema operacional somente posix
print(os.uname)

------------------------------------------------------------------------------

print(os.getcwd()) 
>>> C:\Curso\Curso01

res = os.path.join(os.getcwd(), 'Secao13')
>>> C:\Curso\Curso01\Secao13

os.chdir(res)

print(os.getcwd())

# Veja que o os.path.join() recebe dois parametros, senfo o primeiro o diretorio arua e o segundo o diretorio que sera juntado ao atual.

# Podemos listar os arquivos e diretorios com o listdir()
print(os.listdir('C:/'))

# Podemos listar os arquivos e diretorios com mais detalhes com scandir()
print(list(os.scandir('C:/')))

--------------------------------------------------------------------------

# Podemos listar os arquivos e diretorios com mais detalhes com scandir()
arq = list(os.scandir())

# print(arq)

# print(dir(arq[0]))
print((arq[0].inode())) # Numero do arquivo no diretorio 
print((arq[0].is_dir())) # É um diretorio? False
print((arq[0].is_symlink())) # É um link simbolico? False
print((arq[0].is_file())) # É um arquivo? True
print(arq[0].name) # Nome do arquivo
print(arq[0].path) # Caminho ate o arquivo
print(arq[0].stat()) # Estatisticas do arquivo
"""
import os

# Podemos listar os arquivos e diretorios com mais detalhes com scandir()
arq = list(os.scandir())

# print(arq)

# print(dir(arq[0]))
print((arq[0].inode())) # Numero do arquivo no diretorio 
print((arq[0].is_dir())) # É um diretorio? False
print((arq[0].is_symlink())) # É um link simbolico? False
print((arq[0].is_file())) # É um arquivo? True
print(arq[0].name) # Nome do arquivo
print(arq[0].path) # Caminho ate o arquivo
print(arq[0].stat()) # Estatisticas do arquivo

# OBS: Quando utilizamos a funcao scandir() nos precosamos fecha-la, assim quando abrimos um arquivo.