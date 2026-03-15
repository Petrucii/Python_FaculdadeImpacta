# Programa que lê o valor do saque e informe a quantidade de notas de cada valor que serão distribuídas, considerando as notas de R$ 100, R$ 50, R$ 10, R$ 5 e R$ 1. O valor do saque deve ser entre R$ 10 e R$ 600.

saque = int(input("Digite o valor do saque: "))
valor_minimo = 10
valor_maximo = 600
notas = [100, 50, 10, 5, 1]

n100 = saque // 100
n50 = (saque % 100) // 50
n10 = (saque % 50) // 10
n5 = (saque % 10) // 5
n1 = saque % 5

if saque >= valor_minimo and saque <= valor_maximo:
    print(f"Valor do saque: R$ {saque}, será distrubuído da seguinte forma:")
    print(f"Notas de R$ 100: {n100}")
    print(f"Notas de R$ 50: {n50}")
    print(f"Notas de R$ 10: {n10}")
    print(f"Notas de R$ 5: {n5}")
    print(f"Notas de R$ 1: {n1}")
else:
    print(f"O valor do saque deve ser entre R$ {valor_minimo} e R$ {valor_maximo}.")