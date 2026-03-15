# Programa que lê o tipo e a quantidade de carne comprada e informe o valor a ser pago, sabendo-se que o preço do kg do filé é R$ 4,90 para até 5 kg e R$ 5,80 para mais de 5 kg, o preço do kg da alcatra é R$ 5,90 para até 5 kg e R$ 6,80 para mais de 5 kg, e o preço do kg da picanha é R$ 6,90 para até 5 kg e R$ 7,80 para mais de 5 kg. Se o pagamento for realizado no cartão Tabajara, o cliente receberá um desconto de 5% sobre o valor total da compra. Caso contrário, não haverá desconto.

tipo_carne = input("Digite o tipo de carne (F para filé, A para alcatra, P para picanha): ").lower()
quantidade = float(input("Digite a quantidade de carne (em kg): "))
desconto_cartao = 0.05
desconto = input("Pagamento será realizado no cartão? (S para sim, N para não): ").lower()

if tipo_carne == "f" and quantidade <= 5 and desconto == "s":
    preco_kg = 4.90
    desconto_cartao = 0.05
elif tipo_carne == "f" and quantidade > 5 and desconto == "s":
    preco_kg = 5.80
    desconto_cartao = 0.05
elif tipo_carne == "a" and quantidade <= 5 and desconto == "s":
    preco_kg = 5.90
    desconto_cartao = 0.05
elif tipo_carne == "a" and quantidade > 5 and desconto == "s":
    preco_kg = 6.80
    desconto_cartao = 0.05
elif tipo_carne == "p" and quantidade <= 5 and desconto == "s":
    preco_kg = 6.90
    desconto_cartao = 0.08
elif tipo_carne == "p" and quantidade > 5 and desconto == "s":
    preco_kg = 7.80
    desconto_cartao = 0.05
else:
    if tipo_carne == "f" and quantidade <= 5:
        preco_kg = 4.90
    elif tipo_carne == "f" and quantidade > 5:
        preco_kg = 5.80
    elif tipo_carne == "a" and quantidade <= 5:
        preco_kg = 5.90
    elif tipo_carne == "a" and quantidade > 5:
        preco_kg = 6.80
    elif tipo_carne == "p" and quantidade <= 5:
        preco_kg = 6.90
    elif tipo_carne == "p" and quantidade > 5:
        preco_kg = 7.80

preco_total = quantidade * preco_kg
valor_desconto = preco_total * desconto_cartao
preco_final = preco_total - valor_desconto

print(f"O preço total é: R$ {preco_total:.2f}, o valor do desconto é: R$ {valor_desconto:.2f} e o preço final a ser pago é: R$ {preco_final:.2f}.")