#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Informe um número: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade {}'.format(uni))
print('Dezena {}'.format(dez))
print('Centena {}'.format(cen))
print('Milhar {}'.format(mil))