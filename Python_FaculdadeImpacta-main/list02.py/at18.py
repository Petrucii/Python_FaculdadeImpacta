# Programa que lê uma data no formato dd/mm/aaaa e informe se a data é válida ou não. Considere que o ano é bissexto se for divisível por 4, mas não for divisível por 100, a menos que seja divisível por 400.

data = input("Digite uma data (dd/mm/aaaa): ")

dia, mes, ano = data.split('/')
dia, mes, ano = int(dia), int(mes), int(ano)

dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    dias_por_mes[1] = 29

if (1 <= mes <= 12) and (1 <= dia <= dias_por_mes[mes - 1]):
    print("Data Válida")
else:
    print("Data Inválida")
