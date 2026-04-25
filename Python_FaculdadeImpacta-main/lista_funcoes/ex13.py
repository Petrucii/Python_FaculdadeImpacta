# Função Valida entrada (leiaInt)

def leiaInt(msg):
     while True:
        num = input(msg)
        if num.isnumeric():
            return int(num)
        else:
            print("Entrada inválida. Por favor, digite um número inteiro.")

num = leiaInt("Digite um número inteiro: ")
print(f"O número digitado foi: {num}")
        
