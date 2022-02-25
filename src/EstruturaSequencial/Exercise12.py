# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal
h = float(input('Me diga qual a sua altura: '))

peso_ideal = (72.7 * h) - 58
print(f'Seu peso ideal é: {peso_ideal:.2f}')
