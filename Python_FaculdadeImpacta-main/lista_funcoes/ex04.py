base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

def calcular_area(base, altura):
    area_triangulo = (base * altura) / 2
    return f' A área do triângulo é {area_triangulo}!!'

print(calcular_area(base, altura))

