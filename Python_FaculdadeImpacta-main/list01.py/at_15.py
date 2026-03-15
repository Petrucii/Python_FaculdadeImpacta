# Programa que lê o valor do salário bruto de um funcionário e mostre o valor do salário líquido, sabendo que os descontos são de 11% para o IR, 8% para o INSS, e 5% para o Sindicato.

IR = 11
INSS = 8
Sindicato = 5

salario_bruto = float(input('Digite o valor do seu salário bruto: '))

desconto_ir = salario_bruto * (IR / 100)
desconto_inss = salario_bruto * (INSS / 100)
desconto_sindicato = salario_bruto * (Sindicato / 100)

salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato

print(f'Com os descontos do IR ({IR}%), INSS ({INSS}%), e do Sindicato ({Sindicato}%), O valor do seu salário líquido é de: R${salario_liquido:.2f}')