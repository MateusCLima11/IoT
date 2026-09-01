notas = []

while True:
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

if notas:
    print("\nNotas cadastradas:")
    for n in notas:
        print(f"- {n}")

    quantidade = len(notas)
    media = sum(notas) / quantidade
    maior = max(notas)
    menor = min(notas)

    notas.sort()
    notas.reverse()

    print(f"\nQuantidade de notas: {quantidade}")
    print(f"Média das notas: {media:.2f}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Notas em ordem decrescente: {notas}")
else:
    print("\nNenhuma nota foi cadastrada.")