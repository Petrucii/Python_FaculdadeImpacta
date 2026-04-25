# Função Escopo de Variáveis
nome = "Marcos"

def apresentar():
    idade = 25

    print(f"Dentro da função: nome = {nome}")
    print(f"Dentro da função: idade = {idade}")

apresentar()

print(f"Fora da função: nome = {nome}")