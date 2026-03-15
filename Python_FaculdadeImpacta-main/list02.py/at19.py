# Programa que lê um número inteiro menor que 1000 e informe a quantidade de centenas, dezenas e unidades do número.

num1 = int(input('Digite um número inteiro menor que 1000: '))

unidade = num1 % 10
dezena = (num1 // 10) % 10
centena = num1 // 100

print(f'O número {num1} tem {centena} centenas, {dezena} dezenas e {unidade} unidades.')