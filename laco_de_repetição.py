carrinho = []

while True:
    produto = float(input('Digite o valor do produto: '))
    if (produto == 0):
        break
    else:
        carrinho.append(produto)

valor_total = sum(carrinho)
print(f'O valor total da compra é: {valor_total:.2f}R$')