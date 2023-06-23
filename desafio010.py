#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto você tem de dinheiro na carteira? '))

dolar = real / 4.77

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
