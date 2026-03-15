# Programa que lê o comprimento dos três lados de um triângulo e informe se o triângulo é equilátero, isósceles ou escaleno.

lado1 = float(input('Digite o comprimento do lado 1 do triângulo: '))
lado2 = float(input('Digite o comprimento do lado 2 do triângulo: '))
lado3 = float(input('Digite o comprimento do lado 3 do triângulo: '))

if lado1 == lado2 and lado2 == lado3:
    print('O triângulo é equilátero.')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.')
    