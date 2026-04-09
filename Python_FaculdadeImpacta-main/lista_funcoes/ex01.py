
print("*******************************")
print("* Validando tamanho da string *")
print("*******************************")

x = int(input("Digite um número de 1 a 100, para verificar se está dentro do mínimo da string: "))
y = int(input("Digite um número de 1 a 100 para verificar se está dentro do máximo da string: "))

#Função que valida tamanho de uma string
def valida_string (string, min, max):
    if len(string) > min and len(string) <= max:
        return True
    else:
        return False

#Testando a função
print(valida_string("Hello", x, y))