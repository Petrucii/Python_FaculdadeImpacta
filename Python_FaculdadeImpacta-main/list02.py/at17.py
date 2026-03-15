# Programa que lê um ano e informe se é bissexto ou não. Um ano é bissexto se for divisível por 4, mas não for divisível por 100, a menos que seja divisível por 400.

ano = int(input('Digite um ano para verificar se é bissexto: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")