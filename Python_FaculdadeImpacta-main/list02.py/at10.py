# Programa que lê a letra correspondente ao período que o aluno estuda e mostre uma mensagem de acordo com a letra digitada.

periodo = input('Digite a letra correspondente ao período que você estuda, (ex: M, V ou N): ').lower()

if periodo == 'm':
    print('Bom dia! Você estuda no período da Manhã.')
elif periodo == 'v':
    print('Boa tarde! Você estuda no período da Tarde.')
elif periodo == 'n':
    print('Boa noite! Você estuda no período da Noite.')
else:
    print('Período inválido!')
