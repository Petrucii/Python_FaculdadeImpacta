# Função Lista com dicionário

produtos = [
    {"nome": "Produto A", "preco": 10.99},
    {"nome": "Produto B", "preco": 50.49},
    {"nome": "Produto C", "preco": 20.00}
]

def produto_mais_caro(produtos):
    produto_caro = produtos[0]
    for produto in produtos:
        if produto["preco"] > produto_caro["preco"]:
            produto_caro = produto
    return produto_caro
produto_caro = produto_mais_caro(produtos)


print(f"O produto mais caro é: {produto_caro['nome']} com preço R${produto_caro['preco']:.2f}")
