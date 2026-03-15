# Programa que lê dois números inteiros e um número real, e mostre:
# a) O produto do dobro do primeiro com metade do segundo.
# b) A soma do triplo do primeiro com o terceiro.
# c) O terceiro elevado ao cubo.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num_real = float(input('Digite um número real: '))

print(f'O produto do dobro do primeiro com metade do segundo é: {(num1 * 2) * (num2 / 2)}')
print(f'A soma do triplo do primeiro com o terceiro é: {(num1 * 3) + num_real}')
print(f'O terceiro elevado ao cubo é: {num_real ** 3}')
