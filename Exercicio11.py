#Peça ao usuário dois valores, e faça um programa que peça qual tipo de operação ele deseja fazer, com esse dois valores.
a = int(input('Digite um valor:'))
b = int(input('Digite outro valor:'))
continua = True
while continua:
    print("""[1] Para soma
[2] Para Multiplicar
[3] Para Maior
[4] Para Novos números
[5] Para sair""")
    op = int(input('Escolha uma operação'))
    if op == 1:
        print(f'A soma entre {a} e {b} é igual a {a+b}!')
        print('')
    elif op == 2:
        print(f' O produto entre {a} e {b} igual a {a*b}!')
        print('')
    elif op ==3:
        if a<b:
            print('B é Maior que A')
            print('')
        elif a>b:
            print('a é Maior que b')
            print('')
    elif op == 4:
        a = int(input('Digite um valor:'))
        b = int(input('Digite outro valor:'))
    elif op == 5:
        continua = False
    print('O jogo acabou')