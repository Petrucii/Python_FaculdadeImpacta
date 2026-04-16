a = float(input("Digite a sua primeira nota: "))
b = float(input("Digite a sua segunda nota: "))
c = float(input("Digite a sua terceira nota: "))

def verifica_media(a,b,c):
    media = (a + b + c) / 3
    return media

print(f"A sua media é {verifica_media(a,b,c)}")