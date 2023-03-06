from random import randint


def uniao_vetor(**kwargs):
    vetor_1 = kwargs['vetor_1']
    vetor_2 = kwargs['vetor_2']
    vetor_3 = set()
    vetor_3 = vetor_3.union(vetor_1).union(vetor_2)
    return vetor_3

tam = 10

vetor_1 = [randint(0, 100) for i in range(tam)]
vetor_2 = [randint(0, 100) for i in range(tam)]

print(f'Vetor 1: {vetor_1}, Vetor 2: {vetor_2}')
print(f'Uniao dos vetores: {uniao_vetor(vetor_1=vetor_1, vetor_2=vetor_2)}')