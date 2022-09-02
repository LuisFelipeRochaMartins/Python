#Desenvolva um proograma que leia 6 números int e mostre a soma apenas daqueles que forem pares.#
soma = 0 #
for k in range(1,7,1):
    if k == 1:
        a = int(input('Digite um valor: '))
    else:
        a = int(input('Digite outro número:'))
        if (a % 2 == 0):
            soma+=a 
print(f'A soma dos números pares resultou em {soma}')