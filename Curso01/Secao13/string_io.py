"""
StringIO

ATENCAO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa de permisao:
    - Permisao de Leitura -> Para ler o arquivo.
    - Permisao de Escrita -> Para escrever o arquivo
    
StringIO -> Utilizado para ler e criar arquivos em memoria.

# Primeiro fazemos o import 
from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# Podemos criar uma arquivo em memoria ja com uma string inserida ou mesmo vazio inserirmos texto depois 

arq = StringIO(mensagem)

print(arq.read())

arq.write(' Outro texto')

arq.seek(0)

print(arq.read())
"""

