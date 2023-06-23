#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o salario do funcionário? R$'))

if salario >= 1250:
    novo_salario = salario + (salario * 15 / 100)
else:
    novo_salario = salario + (salario * 10 / 100)

print('O salário do funcionário aumentou de R${:.2f} para R${:.2f}'.format(salario, novo_salario))
