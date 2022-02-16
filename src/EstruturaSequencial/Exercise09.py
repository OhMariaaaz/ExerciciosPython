# Faça um Programa que peça a temperatura
# em graus Fahrenheit, transforme e mostre a temperatura em
# graus Celsius.

temp = float(input('Digite a temperatura em Fahrenheit: '))
tempconvert = 5 * ((temp - 32) / 9)
print('A temperatura em Celsius é: ', tempconvert)
