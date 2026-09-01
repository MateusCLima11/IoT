numeros = []

for i in range(6):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)

soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)

numeros.sort()

print(f"\nSoma dos números: {soma}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Números em ordem crescente: {numeros}")