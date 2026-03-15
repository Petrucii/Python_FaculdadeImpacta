# Programa que lê a primeira letra do sexo e informe se é Masculino ou Feminino.

sexo = input('Digite a primeira letra do seu Sexo, (ex: M ou F): ')

if sexo == 'M' or sexo == 'm':
    print('Você é do Sexo Masculino.')
elif sexo == 'F' or sexo == 'f':
    print('Você é do Sexo Feminino.')
else:
    print('Sexo Inválido.')