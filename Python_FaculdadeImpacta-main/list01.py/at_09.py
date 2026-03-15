# Programa que lê uma temperatura em Fahrenheit e mostre a temperatura convertida em Celsius. A fórmula para converter de Fahrenheit para Celsius é: C = 5 * ((F - 32) / 9), onde C é a temperatura em Celsius e F é a temperatura em Fahrenheit.

F = float(input('Digite a temperatura em Fahrenheit: '))  
C = 5* ((F - 32) / 9)

print(f'A conversão da temperatura de {F}F, é igual a {C}C!')