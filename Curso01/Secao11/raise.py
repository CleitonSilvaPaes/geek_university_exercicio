"""
Levantando os proprios erros com raise

raise -> Lanca excecoes

OBS: O raise nao e um funcao. É uma palavra reservada, assim como o def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo util para que possamos criar nossas proprias excecoes e mensagens de error.

A forma geral de utilizacao e:

raise TipoDoErro('Mensagem de error')

# Exemplo real
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} sera impresso na cor {cor}')
    
colore(True, 'azul')

"""

