idade = int(input('Digite a idade: '))
tempo_servico = int(input('Digite tempo de servico: '))

if idade >= 65 or tempo_servico >= 30 \
    or (idade >= 60 and tempo_servico >= 25):
    print('Pode se aposentar')
else:
    print('Nao pode se aposentar')