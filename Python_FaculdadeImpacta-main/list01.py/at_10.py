# Programa que lê uma temperatura em Celsius e mostre a temperatura convertida em Fahrenheit. A fórmula para converter de Celsius para Fahrenheit é: F = (C * 9/5) + 32, onde F é a temperatura em Fahrenheit e C é a temperatura em Celsius.

C = float(input('Digite a temperatura em Celsius: '))  
F = (C * 9/5) + 32

print(f'A conversão da temperatura de {C}C, é igual a {F}F!')