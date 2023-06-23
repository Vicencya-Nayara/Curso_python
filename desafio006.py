#Crie um algortimo que leia um número e mostre seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))

dobro = num * 2
triplo = num * 3
raizq = num ** (1/2)

print('O dobro do número {} é {} seu triplo é {} e sua raiz quadrada é {}'.format(num, dobro, triplo, raizq))