#Faça um programa que peça ao usuário quantos termos da sequência de Fibonacci ele deseja ver.
n= int(input('digite a quantidade termos que quer na sequência'))
t=int(1)
x= 0
y = z = 1
while t<=(n+1):
    print('O {} termo é igual a {}'.format(t,x))
    z = x+y
    x = y
    y = z
    t+=1