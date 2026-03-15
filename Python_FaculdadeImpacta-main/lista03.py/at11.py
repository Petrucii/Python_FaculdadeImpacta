# Jogo da Forca

palavras = ["America", "Brasil", "Canadá", "Dinamarca", "Espanha", "França", "Grécia", "Holanda", "Itália", "Japão"]
num = int(input("Digite um número de 0 a 9 para sortear uma palavra: "))

palavra_sorteada = palavras[num].lower()
letra_acertadas = []

for letra in palavra_sorteada:
    letra_acertadas.append("_")

tentativas = 6
letras_erradas = ""

while tentativas > 0 and "_" in letra_acertadas:
    palavra_exibida = ""
    for letra in letra_acertadas:
        palavra_exibida += letra + " "

    print(f"A palavra referente ao número {num} é: {palavra_exibida.strip()}")
    print(f"Você tem {tentativas} tentativas restantes.")
    print(f"Letras escolhidas: {letras_erradas}")

    chute = input("Digite uma letra: ").lower()

    if chute in letras_erradas or chute in letra_acertadas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    letras_erradas += chute + " "

    if chute in palavra_sorteada:
        for i in range(len(palavra_sorteada)):
            if palavra_sorteada[i] == chute:
                letra_acertadas[i] = chute
        print("Boa! Você acertou uma letra.")
    else:
        tentativas -= 1
        print("Ops! Letra errada.")

if "_" not in letra_acertadas:
    print(f"Parabéns! Você acertou a palavra {palavra_sorteada.upper()}!")
else:
    print(f"Game Over! A palavra era {palavra_sorteada.upper()}.")
    

