# Programa que lê a quantidade de metros quadrados a serem pintados, e mostre a quantidade de latas de tinta necessárias para o serviço, sabendo que cada lata de tinta tem 18 litros, custa R$ 80,00, e que cada litro de tinta pinta 3 metros quadrados.

litros_por_lata = 18
valor_lata = 80
metro_por_litro = 3

cobertura = metro_por_litro * litros_por_lata

metros = float(input('Digite a quantidade de metros quadrados a serem pintados: '))

latas_necessarias = metros // cobertura
if metros % cobertura > 0:
    latas_necessarias += 1

valor_total = latas_necessarias * valor_lata

print(f'Você precisará de {latas_necessarias:.0f} latas de tinta, o que custará R${valor_total:.0f}')
