#Faça um programa que receba um valor do usuário, e mostre sua tabuada. Caso o usuário informe um valor menor que 0, o programa termina.
continua = True
while continua:
    n=int(input('Digite um valor:'))
    if n <0:
        continua=False
    else:
        for k in range(0,11):
            print(f"{n} x {k} = {n*k}")
print('Programa abortado!')