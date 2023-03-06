def tamanho(txt:str):
    count = 0
    for i in txt:
        count += 1
    return count

txt = input('Digite o texto: ')
print('Texto: ', *txt, f', tamanho: {tamanho(txt)}')