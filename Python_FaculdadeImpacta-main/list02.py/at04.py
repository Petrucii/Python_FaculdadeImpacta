# Programa que lê uma letra do alfabeto e informe se é Vogal ou Consoante.

letra = input('Digite qualquer letra do alfabeto, para descobrir se ela é uma Vogal ou uma consoante: ').lower()

'''if letra in 'aeiou':
    print(f'A letra {letra} digitada, é uma Vogal.')'''

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'A letra {letra} digitada, é uma Vogal.')
else:
    print(f'A letra {letra} digitada, é uma Consoante.')