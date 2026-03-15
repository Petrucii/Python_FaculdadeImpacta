# Programa que lê o preço de três produtos e informe qual é o mais barato.

produto1 = float(input('Qual é o preço do primeiro produto? R$ '))
produto2 = float(input('Qual é o preço do segundo produto? R$ '))
produto3 = float(input('Qual é o preço do terceiro produto? R$ '))

if produto1 < produto2 and produto1 < produto3:
    print(f'Eu gostaria de levar o primeiro produto, que é mais barato, e custa R$ {produto1:.2f}.')
elif produto2 < produto1 and produto2 < produto3:
    print(f'Eu gostaria de levar o segundo produto, que é mais barato, e custa R$ {produto2:.2f}.')
else:
    print(f'Eu gostaria de levar o terceiro produto, que é mais barato, e custa R$ {produto3:.2f}.')