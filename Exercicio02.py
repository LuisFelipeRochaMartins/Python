#Faça um programa que peça ao usuário um número e diga se ele digitou o mesmo número do computador.
from random import randint
rand = randint(0,5)
print('Tente Adivinhar um número de 0 a 5')
n = int(input('Digite um número'))
if n==rand :
    print('Você ganhou')#
else:
    print('A máquina venceu')