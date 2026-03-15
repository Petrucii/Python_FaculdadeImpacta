# Programa que lê quanto você ganha por hora e quantas horas trabalha por mês, e mostre o valor do seu salário mensal.

ganho_hora = int(input('Digite quanto você ganha por hora: R$'))
horas_trabalhadas = float(input('Digite quantas horas você trabalha por mês: '))

salario = ganho_hora * horas_trabalhadas

print(f'Você ganha R$:{salario} por mês!!')