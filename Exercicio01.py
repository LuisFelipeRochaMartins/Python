# Faça um programa que peça 4 notas, calcule sua média e ao final dê a mensagem ao aluno se passou ou não.

n1 = float(input('Digite sua nota:'))#
n2 = float(input('Digite sua outra nota:'))#
n3 = float(input('Digite sua outra nota:'))#
n4 = float(input('Digite sua outra nota:'))#
m = (n1+n2+n3+n4)/4#
if m >= 6.0:#
    print(f'Você passou de nesta matéria, pois teve média de {m}!')#
else:#
    print('Você infelizmente não passou nesta matéria, pois teve média {m}!')#