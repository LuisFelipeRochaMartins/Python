#Escreva um programa que leia a velocidade de um carro, se ela ultrapassar#
#80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km#
velo= int(input('Digite a velocidade do carro'))
if (velo > 80):
    print('Você recebeu uma multa por andar acima da velocidade permitida, a multa é de R$ {}!'.format((velo-80)*7))
else:
    print('Velocidade dentro do limite, tenha uma Boa Viagem!')