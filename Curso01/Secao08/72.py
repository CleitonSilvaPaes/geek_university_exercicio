def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(num)
        except Exception:
            valid.append(None)
    return valid if None not in valid else []


def soma_vetores(**kwargs):
    v1, v2 = kwargs['v1'], kwargs['v2']
    soma = []
    for i in range(len(v1)):
        tmp = v1[i] + v2[i]
        soma.append(tmp)
    return soma
                    
vetor1 = isint(*input('Digite valores para o Vetor 1 separado por espaco: ').split())
vetor2= isint(*input('Digite valores para o Vetor 2 separado por espaco: ').split())

if vetor1 and vetor2 and len(vetor1) == len(vetor2):
    print(soma_vetores(v1=vetor1, v2=vetor2))
else:
    print('Digite valores valido e de tamanho iguais')