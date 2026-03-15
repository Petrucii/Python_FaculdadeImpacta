# Informando se é Palindromo ou não

palindromo = input("Digite qualquer palavra para verificar se é um palíndromo: ").lower().replace(" ", "")

if palindromo == palindromo[::-1]:
    print(f"A palavra '{palindromo}' é um palíndromo.")
else:
    print(f"A palavra '{palindromo}' não é um palíndromo.")
