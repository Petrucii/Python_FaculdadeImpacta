# Mostrando número por extenso

num = int(input("Digite um número até 99, e o programa escreverá por extenso: "))

unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]

dezenas = ["dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

if num < 10:
    print(f"O número {num} por extenso é: {unidades[num]}")
elif num < 100:
    dezena = (num // 10) - 1
    unidade = num % 10
    if unidade == 0:
        print(f"O número {num} por extenso é: {dezenas[dezena]}")
    else:
        print(f"O número {num} por extenso é: {dezenas[dezena]} e {unidades[unidade]}")