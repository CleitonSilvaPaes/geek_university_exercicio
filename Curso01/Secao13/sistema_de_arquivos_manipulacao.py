"""
Sistema de Arquivos - Manipulação


# Descobrindo se um arquivo ou diretorio existe

print(os.path.exists('Curso01'))
>>> True
print(os.path.exists('arquivo.txt'))
>>> False

--------------------------------------------------------------------------------

# Criando arquivos
os.mknod('arquivo-teste.txt') # Funciona somente no sistemas posix

# OBS: Se voce estiver utilizando no Mac OS, pode haver um erro de
# Permissioon Error
# Criando um arquivo via mknod() se o arquivo ja existir teremos o error FiliExistsError

--------------------------------------------------------------------------------

# Criando Diretorios - unicos (um a um)

# Relativo
os.mkdir('templates')

#Abusoluto
os.mkdir('c:/Curso/Curso01/Secao13/template')

# OBS: A funcao mkdir() cria um diretorio se este nao existir. Caso exista, teremos FileExistsError 
# Se nao tivermos permisao oara criar o diretorio teremos um PermissionError

--------------------------------------------------------------------------------

Criando nulti-diretorios (arvore de diretorios)
os.makedirs('templates/geek/university/)

# OBS: Se ja existir, teremos um FileExistsError

--------------------------------------------------------------------------------

# Renomear arquivos e diretorios
os.rename('nome_do_arquivo', 'nome_desejado')

# OBS: So diretorio nao existir teremos um FileNotFoundError

# Se o diretorio que queremos renomear nao estiver vazio, teremos um OSError

--------------------------------------------------------------------------------

# ATENCAO! Tome cuidado com os comandos de delecoa. Ao deletarmos um arquivo ou diretorio, eles nao vao para a lixeira. Eles somem

os.remove('nome_do_arquivo')

# OBS: Se voce estiver no windown e o arquivo que voce for deletar estiver em uso, voce tera um erro.
# Caso o arquivo nao exista, Teremos o FileNotFoundError

--------------------------------------------------------------------------------


# Removendo diretorios vazio
os.rmdir('nome_diretorio')

# OBS: Se o diretorio nao existir teremos um FileNotFoundError

os.removedirs('nome_do_diretorio/outro_diretorios')

# Se algum dos diretorios contiver arquivos ou outros diretorios, o processo para.

--------------------------------------------------------------------------------

# Trabalhando com arquivos e diretorios temporarios
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretorio temporario em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arq:
        arq.write('Cleiton Silva Carvalho Paes\n')
    input()
    
# Estamos criando um diretorio temporario, abrindo o menmo e dentro dele criando um arquivo para escrevermos um texto. No final, usamos um input() so para mantwemos os arquivos temporarios 'vivos' dentreo dos blocos with.

--------------------------------------------------------------------------------

# Criando um arquivo temporario
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())
    
# OBS: Em arquivos temporatios so conseguimos escrever bits. Por isso, utilizamos b''

https://docs.python.org/3/library/os.html?highlight=os#module-os
"""
# Trabalhando com arquivos e diretorios temporarios
import os
import tempfile

