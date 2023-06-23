#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possivéis sobre ela

algo = input('Digite algo: ')
print(type(algo))
print('Só tem espaços?' ,algo.isspace())
print('É um numero?' ,algo.isnumeric())
print('é alfabetico?' ,algo.isalpha())
print('é alfanumerico?' ,algo.isalnum())
print('esta em maiusculas?' ,algo.isupper())
print('esta em minusculas' ,algo.islower())
print('esta capitalizada?' ,algo.isprintable())