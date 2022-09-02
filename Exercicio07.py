#Crie uma tabuada com um número fornecido pela usuário#
i=int(input('Digite um número:'))
for k in range(0,11,1):
    print(f'{i} x  {k} = {k*i}')
