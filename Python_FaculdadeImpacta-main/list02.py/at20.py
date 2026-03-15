# Programa que lê as três notas de um aluno, calcula a média e mostre a situação do aluno de acordo com a média, mostrando a menção correspondente a cada faixa de média.

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media >= 10:
    print("Aprovado com distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
