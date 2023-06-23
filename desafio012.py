#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: '))

novo_preco = preco  - (preco * 5 / 100)

print('O preço do produto que custava R${:.2f} e com 5% de desconto irá custar R${:.2f}'.format(preco, novo_preco))