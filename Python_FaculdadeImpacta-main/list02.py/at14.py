# Mostrando a situação do aluno de acordo com a média de duas notas digitadas pelo usuário, e mostrando a menção correspondente a cada faixa de média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    print(f'Parabéns! Você foi aprovado com a média {media:.2f} e recebeu a menção "A".')
elif media >= 7.5 and media < 9:
    print(f'Você foi aprovado com a média {media:.2f} e recebeu a menção "B".')
elif media >= 6 and media < 7.5:
    print(f'Você foi aprovado com a média {media:.2f} e recebeu a menção "C".')
elif media >= 4 and media < 6:
    print(f'Você foi reprovado com a média {media:.2f} e recebeu a menção "D".')
elif media >= 0 and media < 4:
    print(f'Você foi reprovado com a média {media:.2f} e recebeu a menção "E".')