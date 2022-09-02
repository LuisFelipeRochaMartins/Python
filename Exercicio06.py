#Faça um programa que calcule a soma entre todos os números ímares que são multilos de três e que se encontram no invervalo ed 1 a 500#
soma = 0
for k in range(1,501,+2):
    if (k % 3==0):
        soma+=k
print(f'Há {soma} números múltiplos de 3 no intervalo entre 1 e 500')