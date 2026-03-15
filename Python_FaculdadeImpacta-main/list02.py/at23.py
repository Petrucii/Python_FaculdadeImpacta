# Programa que lê um número e informe se ele é inteiro ou decimal.

num1 = float(input("Digite um número para ver se ele é inteiro ou decimal: "))
if num1 % 1 == 0:
    print(f"O número {num1} é inteiro.")
else:
    print(f"O número {num1} é decimal.")