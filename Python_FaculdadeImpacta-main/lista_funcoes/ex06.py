numero = int(input("Digite um número inteiro: "))

def verificar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
print(verificar(numero))