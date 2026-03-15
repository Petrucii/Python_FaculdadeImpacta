# Programa que lê a quantidade de metros quadrados a serem pintados, e mostre a quantidade de latas de tinta necessárias para o serviço, sabendo que cada lata de tinta tem 18 litros, custa R$ 80,00, e que cada litro de tinta pinta 3 metros quadrados. Considere ainda que a loja vende também galões de tinta de 3.6 litros, que custam R$ 25,00. O programa deve mostrar as quantidades de latas e galões necessárias para o serviço, bem como o preço total. Obs: considere sempre uma folga de 10% na hora de calcular a quantidade de tinta necessária.

litros_por_lata = 18
litros_por_galao = 3.6
valor_lata = 80
valor_galao = 25
metro_por_litro = 6

metros = float(input('Digite a quantidade de metros quadrados a serem pintados: '))

areaFolga = metros * 1.1
litros_necessarios = areaFolga / metro_por_litro

latas_necessarias = int(litros_necessarios // litros_por_lata)

litros_restantes = litros_necessarios % litros_por_lata

galoes_necessarios = int(litros_restantes // litros_por_galao)

if litros_restantes % litros_por_galao > 0:
    galoes_necessarios += 1


valor_total = (latas_necessarias * valor_lata) + (galoes_necessarios * valor_galao)
print(f'Você precisará de {latas_necessarias:.0f} latas de tinta, e {galoes_necessarios} galão(ôes), o que custará R${valor_total:.2f}!!')