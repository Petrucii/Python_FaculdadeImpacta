# Jogo de adivinhação de palavras embaralhadas

palavra_embaralhada = "mrcaiae"
palavra_correta = "america"

tentativa = input(f"Descubra qual é a palavra embaralhada: '{palavra_embaralhada}'\nDigite sua resposta: ").lower()

'''if tentativa == palavra_correta:
    print("Parabéns! Você acertou a palavra.")
else:
    print("Que pena! Tente novamente.")'''

while tentativa != palavra_correta:
    print("Que pena! Tente novamente.")
    tentativa = input(f"Descubra qual é a palavra embaralhada: '{palavra_embaralhada}'\nDigite sua resposta: ").lower()

if tentativa == palavra_correta:
    print(f"Parabéns! Você acertou, a palavra embaralhada '{palavra_embaralhada}' é '{palavra_correta}'.")