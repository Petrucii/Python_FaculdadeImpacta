#Mostrando nome em escada crescente

nome = input("Digite seu nome: ").upper()

for i in range(0, len(nome) + 1):
    print(nome[:i])