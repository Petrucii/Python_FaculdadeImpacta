a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))

def maior_valor(a,b):
    if a > b:
        return f"O maior número entre os dois digitados é: {a}"
    else:
        return f"O maior número entre os dois digitados é: {b}"

print(maior_valor(a,b))
