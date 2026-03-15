# Programa que lê o tamanho do lado de um quadrado e mostre o dobro da área total do quadrado. A fórmula para calcular a área do quadrado é: A = l^2, onde A é a área e l é o lado.

lado = int(input('Digite o tamanho do lado de um quadrado, para descobrir o tamanho da sua área: '))

area = (lado ** 2) * 2

print(f'O dobro da área total de um quadrado com o tamanho {lado} de lado, é igual a: {area}!')