nome =  input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

'''print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")'''


print(f'Seu nome é {nome}, e você tem {idade} anos!\n')

if idade <= 30:
    print(f'Muito prazer {nome}, {idade} anos, você é bem jovem ainda em!!')

elif idade >=31 and idade <= 59:
    print(f'Muito prazer {nome}, {idade} anos, você tem muita lenha pra queimar ainda em!!! rsrs')

else:
    print(f'Muito prazer {nome}, {idade} anos, a sua experiência de vida é muito')