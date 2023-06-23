#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperaturaC = float(input('Qual a temperatura em celcius: '))

fahrenheit =  9 * temperaturaC / 5 + 32
print('a temperatura de {}°C corresponde a {}°F'.format(temperaturaC, fahrenheit))