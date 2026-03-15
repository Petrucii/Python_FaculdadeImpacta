# Mostrando o maior e o menor número entre três números digitados pelo usuário.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    '''print(f'O maior número é o {num1}.')'''
    maiorNum = num1
elif num2 > num1 and num2 > num3:
    '''print(f'O maior número é o {num2}.')'''
    maiorNum = num2
else:
    '''print(f'O maior número é o {num3}.')'''
    maiorNum = num3

if num1 < num2 and num1 < num3:
    '''print(f'O menor número é o {num1}.')'''
    menorNum = num1
elif num2 < num1 and num2 < num3:
    '''print(f'O menor número é o {num2}.')'''
    menorNum = num2
else:
    '''print(f'O menor número é o {num3}.')'''
    menorNum = num3

print(f'O maior número é o {maiorNum}, e o menor número é o {menorNum}.')

'''maiorNum = num1 > num2 and num1 > num3
menorNum = num1 < num2 and num1 < num3'''