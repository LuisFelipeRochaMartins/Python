#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores mf. caso esteja errado, pela a digitação novamente.

#Strip para tirar os espaços indesejáveis, e upper para ignorar o tipo de Case que o usuário fornece.
sexo = str(input('Digite seu sexo:')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Digite novamente seu sexo:')).strip().upper()[0]
print(f'Valor validado sexo = {sexo}')