notas = []

for i in range(1, 9):
    nota = float(input(f"Digite a nota do {i}º aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

notas_acima_da_media = [nota for nota in notas if nota > media]

print(f"\nMédia aritmética da turma: {media:.2f}")
print(f"Notas acima da média: {notas_acima_da_media}")