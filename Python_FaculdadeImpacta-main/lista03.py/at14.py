# Convertendo texto para Leet Speak

txt = input("Digite um texto para converter: ").lower()
leet = ""

for i in txt:
    if i in "Aa":
        leet += "4"
    elif i in "Ee":
        leet += "3"
    elif i in "Ii":
        leet += "1"
    elif i in "Oo":
        leet += "0"
    elif i in "Ss":
        leet += "5"
    else:
        leet += i

print(f"A sua palavra original é: '{txt}', e a palavra convertida é '{leet.upper()}'!")

