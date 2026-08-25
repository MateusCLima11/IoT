import random

nomes = []

for i in range(1, 11):
    nome = input(f"Digite o {i}º nome: ")
    nomes.append(nome)

nome_sorteado = random.choice(nomes)

# Exibição do resultado
print(f"\nO nome sorteado foi: {nome_sorteado}")