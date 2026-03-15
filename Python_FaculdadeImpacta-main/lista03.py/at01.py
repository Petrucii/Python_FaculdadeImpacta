#mostrando o conteúdo e o tamanho de cada String, se possuem o mesmo tamanho e se o conteúdo é igual ou diferente.

txt1 = input("Digite uma palavra: ")
txt2 = input("Digite outra palavra: ")

if txt1 > txt2:
    print(f"A palavra '{txt1}', tem {len(txt1)} caracteres e é maior que a palavra '{txt2}'.")
elif txt1 < txt2:
    print(f"A palavra '{txt2}', tem {len(txt2)} caracteres e é maior que a palavra '{txt1}'.")
else:
    print(f"As palavras '{txt1}' e '{txt2}' são iguais, ambas têm {len(txt1)} caracteres.")