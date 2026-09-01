produtos = []

for i in range(5):
    produto = input(f"Digite o nome do produto {i + 1}: ")
    produtos.append(produto)

print("\nLista de produtos cadastrados:", produtos)
print("Quantidade total de produtos:", len(produtos))