def isfloat(*args):
    valid = []
    for i in args:
        try:
            float(i)
            valid.append(float(i))
        except:
            valid.append(False)
    return valid if False not in valid else []
    
def calc_media(letra:str, *args):
    letra = letra.lower()
    if len(args) == 3:
        if letra == 'a':
            return sum(args) / len(args)
        elif letra == 'b':
            media = ((args[0] * 5) + (args[1] * 3) + (args[2] * 2)) / 10
            return media
        return 'letra informada invalida'


rodar = True
while rodar:
    provas = []
    print("""
Informe a opcao:
    
(a) - Media Aritimetrica
(b) - Media Ponderada """)
    opcao = input()
    for i in range(3):
        nota = input(f'Digite nota {i+1}: ')
        provas.append(nota)
    if isfloat(*provas):
        rodar = False
        provas = isfloat(*provas)
        print(calc_media(opcao, *provas))
    else:
        print('Notas no formato invalido')