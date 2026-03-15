# Programa que lê um número de 1 a 7 e informe o dia da semana correspondente a esse número. Caso o número seja inválido, informe que não existe dia da semana correspondente.

num_semana = int(input(('Digite um número de 1 a 7 para saber o dia da semana: ')))
if num_semana == 1:
    print('Domingo')
elif num_semana == 2:
    print('Segunda-feira')
elif num_semana == 3:
    print('Terça-feira')
elif num_semana == 4:
    print('Quarta-feira')
elif num_semana == 5:
    print('Quinta-feira')
elif num_semana == 6:
    print('Sexta-feira')
elif num_semana == 7:
    print('Sábado')
else:
    print('Número inválido. Por favor, digite um número de 1 a 7.')