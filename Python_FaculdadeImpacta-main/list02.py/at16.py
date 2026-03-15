# Programa que lê os coeficientes a, b e c de uma equação do segundo grau e mostre a equação, o valor do delta e as raízes, se existirem. Caso a seja igual a zero, informe que a equação não é de segundo grau e encerre o programa.

a = float(input("Digite o valor de a: "))

if a == 0:
    print(f"A equação não é de segundo grau, encerrando o programa.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c
    eq_segundo_grau = f"{a}x² + {b}x + {c} = 0"

    if delta < 0:
        print(f"A equação {eq_segundo_grau} é negativa e não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação {eq_segundo_grau} é do segundo grau e possui uma raiz real: x = {raiz:.2f}.")
    else:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        print(f"A equação {eq_segundo_grau} é do segundo grau e possui duas raízes reais: x1 = {raiz1:.2f} e x2 = {raiz2:.2f}.")