# Programa que lê dois números e uma operação (soma, subtração, multiplicação ou divisão) e mostre o resultado da operação. Em seguida, informe se o resultado é inteiro ou decimal, par ou ímpar, positivo ou negativo.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ") 

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero não é permitida."

else:
    resultado = "Operação inválida."
if resultado % 1 == 0:
    print(f"O número {resultado} é inteiro.")
else:
    print(f"O número {resultado} é decimal.")

if resultado % 2 == 0:
    print(f"O número {resultado} é par.")
else:
    print(f"O número {resultado} é ímpar.")

if resultado > 0:
    print(f"O número {resultado} é positivo.")
else:
    print(f"O número {resultado} é negativo.")


print(f"O Resultado é: {resultado}!")