# Programa que lê o valor do salário de um funcionário e calcule o valor do aumento e o novo salário, de acordo com as seguintes regras:

salario = float(input('Digite o valor do seu salário: R$ '))

if salario <= 280:
    aumento = salario * 0.20
    novo_salário = salario + aumento
    print(f'O salário antes do reajuste era R$ {salario:.2f}, teve um aumento aplicado de 20%, resultando no valor do aumento de R$ {aumento:.2f} e o novo salário é R$ {novo_salário:.2f}.')
elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
    novo_salário = salario + aumento
    print(f'O salário antes do reajuste era R$ {salario:.2f}, teve um aumento aplicado de 15%, resultando no valor do aumento de R$ {aumento:.2f} e o novo salário é R$ {novo_salário:.2f}.')
elif salario > 700 and salario <= 1500:
    aumento = salario * 0.10
    novo_salário = salario + aumento
    print(f'O salário antes do reajuste era R$ {salario:.2f}, teve um aumento aplicado de 10%, resultando no valor do aumento de R$ {aumento:.2f} e o novo salário é R$ {novo_salário:.2f}.')
else:
    aumento = salario * 0.05
    novo_salário = salario + aumento
    print(f'O salário antes do reajuste era R$ {salario:.2f}, teve um aumento aplicado de 5%, resultando no valor do aumento de R$ {aumento:.2f} e o novo salário é R$ {novo_salário:.2f}.')