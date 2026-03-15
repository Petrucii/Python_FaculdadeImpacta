# Programa que lê um número inteiro e informe se ele é par ou ímpar.

num1 = int(input("Digite um número para ver se ele é par ou ímpar: "))
if num1 % 2 == 0:
    print(f"O número {num1} é par.")
else:
    print(f"O número {num1} é ímpar.")