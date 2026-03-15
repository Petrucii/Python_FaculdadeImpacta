# Programa que lê o valor da hora de trabalho e a quantidade de horas trabalhadas no mês, calcule o salário bruto, o valor do imposto de renda, do sindicato, do INSS, o salário líquido e os descontos.

valor_hora = float(input('Digite o valor da sua hora de trabalho: R$ '))
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas no mês: '))
salario_bruto = valor_hora * horas_trabalhadas
impRenda = salario_bruto * 0.11
sindicato = salario_bruto * 0.03
inss = salario_bruto * 0.11
salario_liquido = salario_bruto - impRenda - sindicato - inss
total_descontos = impRenda + sindicato + inss
if salario_bruto <= 900:
    print(f'O salário bruto é de R$ {salario_bruto:.2f} e o salário líquido é de R$ {salario_liquido:.2f}, você está isento do pagamento do Imposto de Renda.')
elif salario_bruto > 900 and salario_bruto <= 1500:
    print(f'O salário bruto é de R$ {salario_bruto:.2f}, você tem um total de descontos de R$ {total_descontos:.2f}, sendo R$ {impRenda:.2f} do Imposto de Renda, R$ {sindicato:.2f} do Sindicato e R$ {inss:.2f} do INSS, e o salário líquido é de R$ {salario_liquido:.2f}.')
elif salario_bruto > 1500 and salario_bruto <= 2500:
    print(f'O salário bruto é de R$ {salario_bruto:.2f}, você tem um total de descontos de R$ {total_descontos:.2f}, sendo R$ {impRenda:.2f} do Imposto de Renda, R$ {sindicato:.2f} do Sindicato e R$ {inss:.2f} do INSS, e o salário líquido é de R$ {salario_liquido:.2f}.')
else:
    print(f'O salário bruto é de R$ {salario_bruto:.2f} e o salário líquido é de R$ {salario_liquido:.2f}, você tem um desconto de 10% do Imposto de Renda, que é de R$ {impRenda:.2f}.')