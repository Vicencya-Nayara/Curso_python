#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

num = float(input('digite um número: '))

print('o número {} tem a parte inteira {}'.format(num, trunc(num)))