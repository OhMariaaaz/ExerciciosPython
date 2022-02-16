# Faça um Programa que peça 2 números inteiros e um número real. Calcule e
# mostre:
#  a. o produto do dobro do primeiro com metade do segundo.
#  b. a soma do triplo do primeiro com o terceiro.
#  c. o terceiro elevado ao cubo.

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))

print('a: ', (n1*2)*(n2/2))
print('b: ', (n1*3)+n3)
print('c: ', n3**3)
