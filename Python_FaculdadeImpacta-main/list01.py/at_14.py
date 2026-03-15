# Programa que lê a quantidade de kg de peixe pescados, e mostre o valor da multa, sabendo que a multa é de R$ 4,00 por kg excedente, e que o limite de kg de peixe é de 50 kg.

multa = 4.00
kilo = float(input('Digite a quantidade de kg de peixe pescados: '))

if kilo > 50:
    excesso = kilo - 50
    multa = 4.00 * excesso
elif kilo <= 50:
    multa = 0
    excesso = 0

print(f'O pescador pescou {kilo} kg de peixe, e excedeu {excesso} kg, a multa a ser paga é de R$ {multa:.2f}')

