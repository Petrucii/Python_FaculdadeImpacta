# Contando espaços e vogais

frase = input("Digite uma frase: ").lower()
espacos = 0
vogais = 0

for i in frase:
    if i == " ":
        espacos += 1
    elif i in "aãeioõu":
        vogais += 1

print(f"A frase digitada: '{frase}' tem {espacos} espaços, e {vogais} vogais.")
