# Programa que lê o valor do raio de um círculo e mostre o valor da área do círculo. A fórmula para calcular a área do círculo é: A = π * r^2, onde A é a área e r é o raio. Considere π = 3.14.

pi = 3.14
print('Descubra o valor da área de um circulo, escolhendo o valor do raio abaixo!')
raio = float(input('Digite o valor do raio: '))

area = pi *(raio ** 2)


print(f'A área do circulo é igual a: {area}!')