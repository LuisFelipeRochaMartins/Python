#Desenvolva um programa que leia o n1 e a r de uma pa. no final mostre até n10 dessa pa#
n1 = int(input('Digite o primeiro valor dessa P.A.'))
r = int(input('Digite a razão dessa P.A.'))
for k in range(1,11,1):
    if (k==1):
        print('n1 = {}'.format(n1))
else:
    print('n{} = {}'.format(k,n1+(r*k)))