#Faça uma lista que peça os número ao usuário e verifique se esse número está na lista, caso sim, informar ao usuário e 
# não adicionar a lista. 
valores = list()
continua = True
while continua:
    num = int(input('Digite um valor que deseja adicionar no Vetor.'))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado!')
    else:
        print('Valor Duplicado!')
        r = str(input('Deseja continuar? [S/N]')).strip().upper()
        if r == 'N':
            continua = False
valores.sort()
print(valores)