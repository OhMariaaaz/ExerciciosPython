# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, utilizando as seguintes fórmulas:

g = int(input('Mulher (1) | Homem (2)'))
h = float(input('Me diga qual a sua altura: '))
if g != 1 and g != 2:
    print('resposta inválida')
elif g == 1:
    peso_ideal = (62.1 * h) - 58
    print(f'Seu peso ideal é: {peso_ideal:.2f}')
elif g == 2:
    peso_ideal = (72.7 * h) - 58
    print(f'Seu peso ideal é: {peso_ideal:.2f}')
