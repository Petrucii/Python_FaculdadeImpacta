# Programa que lê as notas de um aluno e informe se ele foi aprovado, reprovado ou aprovado com distinção.

nota1 = int(input('Digite a sua primeira nota: '))
nota2 = int(input('Digite a sua segunda nota: '))


media = (nota1 + nota2) / 2

if media == 10:
    print('Aprovado com Distinção!! Sua média é igual a 10.')
elif media >=7 and media <=9:
    print('Aprovado! Sua média é maior ou igual a 7.')
else:
    print('Reprovado! Infelizmente sua média foi menor que 7.')
