# Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês.
import os

os.system('clear')

perhora = float(input('Digite o quando você recebe por hora de trabalho: '))
horas = int(input('Digite quantas horas você trabalhou este mês: '))

print('Você vai receber: ', perhora * horas)
