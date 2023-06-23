#Faça um programa que leiaa um número inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input('Digite um número: '))

antecessor = numero - 1
sucessor = numero + 1

print('O número {} tem como antecessor {} e sucessor {}'.format(numero, antecessor, sucessor))
