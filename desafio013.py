#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual seu salario? '))

novo_salario = salario  + (salario * 15 / 100)

print('O salario era R${:.2f} e com 15% de aumento seu novo salario será R${:.2f}'.format(salario, novo_salario))