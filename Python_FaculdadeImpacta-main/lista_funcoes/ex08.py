#Calculadora de Média de Lista
def calcular_media(*args):
    media = sum(args) / len(args)
    return media

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))

resultado = calcular_media(nota1, nota2, nota3)

print(f"A sua média final é: {resultado:.2f}")
