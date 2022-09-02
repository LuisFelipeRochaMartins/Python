#Faça um programa que simule um Ímpar ou par, podendo escolher entre ímpar ou par, e também peça ao usuário o valor que deseja usar no jogo. 
# e também mostre ao final do jogo a quantidade de vezes que o usuário ganhou da máquina.
import random

ganhando = True
cont = 0
while ganhando:
    op = str(input('Escolhe entre Par ou Ímpar![P/I]')).upper().strip()
    while op not in 'PI':
        print('Escolha inválida!, favor digite novamente')
        op = str(input('Escolhe entre Par ou Ímpar![P/I]')).upper().strip()
    n = int(input('Digite um valor:'))
    rand = random.randint(0,10)
    soma = n + rand
    print(f'Você jogou {n} e o computador {rand}, o total deu {soma}')
    if op == 'P' and (soma%2==0):
        print('Você ganhou!!')
        cont+=1
    elif op=='I'and(soma%2!=0):
        print('Você ganhou!!')
        cont+=1
    else:
        print(f'Você perdeu, mas teve o total de {cont} vitórias!')
        ganhando = False