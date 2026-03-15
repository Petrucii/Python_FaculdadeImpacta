# Ajustando número de telefone fixo para 8 dígitos e formatando com hífen

tel = input("Digite um número de telefone fixo com 7 ou 8 dígitos: ")

tel = tel.replace("-", "")

if len(tel) == 7:
    print(f"O Telefone {tel} tem 7 dígitos. Vou adicionar o número 3 no início.")
    tel_ajustado = "3" + tel
else:
    tel_ajustado = tel

tel_formatado = tel_ajustado[:4] + "-" + tel_ajustado[4:]

print(f"O número de telefone formatado é: {tel_formatado}")