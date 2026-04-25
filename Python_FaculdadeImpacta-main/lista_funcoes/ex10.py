# Função contadora de vogais

frase = input("Digite uma frase: ")

def contar_vogais(frase):
    vogais = 'aeiouAEIOUãÃõÕéÉ'
    contador = 0
    for Letra in frase:
        if Letra in vogais:
            contador += 1
    return contador
resultado = contar_vogais(frase)

print(f"A frase contém {resultado} vogais.")