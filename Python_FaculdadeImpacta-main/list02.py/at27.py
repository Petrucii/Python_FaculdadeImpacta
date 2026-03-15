# Programa que lê a quantidade de morangos e maçãs (em kg) e informe o preço a ser pago, sabendo-se que o preço do kg do morango é R$ 2,50 para até 5 kg e R$ 2,20 para mais de 5 kg, e o preço do kg da maçã é R$ 1,80 para até 5 kg e R$ 1,50 para mais de 5 kg. Se o cliente comprar mais de 8 kg em frutas ou se o valor total da compra ultrapassar R$ 25,00, receberá um desconto de 10% sobre o valor total da compra. Caso contrário, o desconto será de 5%.

morangos = float(input("Digite a quantidade de morangos (em kg): "))
macas = float(input("Digite a quantidade de maçãs (em kg): "))

if morangos <= 5:
    preco_morango = 2.50
    desconto_morango = 0.05
else:
    preco_morango = 2.20
    desconto_morango = 0.10

if macas <= 5:
    preco_maca = 1.80
    desconto_maca = 0.05
else:
    preco_maca = 1.50
    desconto_maca = 0.10

preco_total = (morangos * preco_morango) + (macas * preco_maca)
valor_desconto = preco_total * (desconto_morango + desconto_maca)
preco_final = preco_total - valor_desconto

print(f"O preço total é: R$ {preco_total:.2f}, o valor do desconto é: R$ {valor_desconto:.2f} e o preço final a ser pago é: R$ {preco_final:.2f}.")
