#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
aluno1 = input('informe o nome do primeiro aluno: ')
aluno2 = input('informe o nome do segundo aluno: ')
aluno3 = input('informe o nome do terceiro aluno: ')
aluno4 = input('informe o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem dos alunos sorteados é {}'.format(lista))
