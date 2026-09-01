nomes = []

while True:
    nome = input("Digite um nome (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break
    nomes.append(nome)

nomes.sort()

print("\nLista de nomes em ordem alfabética:", nomes)
print("Quantidade de nomes cadastrados:", len(nomes))