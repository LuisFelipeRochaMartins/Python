from random import randint


def sorteia(lista):
    for k in range(0, 5):
        lista.append(randint(0, 1000))
        print(lista)
        print('Terminei')
        somapar(lista)


def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma = soma + n
            print(f'{soma}')


def fatorial(x, logic=False):
    """"
    faz o Fatorial de algum número
    :param x: o valor a ser fatoriado;
    :param show: mostrar ou não o processo;
    :return: retorna o valor fatorial
    """
    f=1
    for c in range (x,0,-1):
        if logic:
            if c>1:
                print(f'{c} x ',end='')
            else:
                print('=',end='')
        f*=c
    return f