Valor = float(input("Digite o custo do produto: R$"))
taxa = float(input("Digite a taxa do imposto: "))


#Função de Cálculo de Imposto
def soma_imposto(taxa_imposto, custo):
    valor_final = custo * (1 + taxa_imposto /100)
    return valor_final

resultado = soma_imposto(taxa,Valor)
print(f"O valor com imposto é de: R${resultado:.2f}")