#Escreva um programa que leia um valor em metros e exiba convertidos em centimetros e milimetros

med = float(input('Informe uma distância em metros: '))

cm = med * 100
mm = med * 1000

print('A medida de {:.2f}m convertido em centimetros é {:.0f}cm e em milimetros é {:.0f}'.format(med, cm, mm))