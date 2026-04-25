# Função que Inverte uma string
s = input("Digite uma string para inverter: ")

def inverter_string(s):
    return s[::-1]
invertida = inverter_string(s)
print(f"A string invertida é: {invertida}")

