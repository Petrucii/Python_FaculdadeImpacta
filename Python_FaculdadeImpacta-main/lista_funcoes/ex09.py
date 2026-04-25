#Função de coversor de temperatura/ Celcius para Fahrenheit
temp = float(input("Digite a temperatura em Celcius: "))


def conversor_temperatura(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit
resultado = conversor_temperatura(temp)


print(f"A temperatura em Fahrenheit é: {resultado:.2f}°F")
