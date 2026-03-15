# Programa que lê a quantidade de litros vendidos e o tipo de combustível (A para álcool, G para gasolina) e informe o valor a ser pago pelo cliente, sabendo-se que o preço do litro do álcool é R$ 1,90 e o preço do litro da gasolina é R$ 2,50. O desconto para o álcool é de 3% para até 20 litros e 5% para mais de 20 litros. O desconto para a gasolina é de 4% para até 20 litros e 6% para mais de 20 litros.

litros = float(input("Digite a quantidade de litros: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").lower()

if tipo_combustivel <=20 and tipo_combustivel == 'a':
    preco_litro = 1.90
    desconto = 0.03
else:
    preco_litro = 1.90
    desconto = 0.05

if tipo_combustivel <=20 and tipo_combustivel == 'g':
    preco_litro = 2.50
    desconto = 0.04
else:
    preco_litro = 2.50
    desconto = 0.06

preco_total = litros * preco_litro
valor_desconto = preco_total * desconto
preco_final = preco_total - valor_desconto

print(f"O preço total é: R$ {preco_total:.2f}, o valor do desconto é: R$ {valor_desconto:.2f} e o preço final a ser pago é: R$ {preco_final:.2f}.")