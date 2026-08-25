numeros = []
negativos = []
soma_positivos = 0
qtd_positivos = 0
qtd_negativos = 0

# Leitura dos 10 números
for i in range(1, 11):
    num = float(input(f"Digite o {i}º número: "))
    
    if num > 0:
        qtd_positivos += 1
        soma_positivos += num
    elif num < 0:
        qtd_negativos += 1
        negativos.append(num)

# Exibição dos resultados
print("\n--- Resultados ---")
print(f"Quantidade de números positivos: {qtd_positivos}")
print(f"Soma dos números positivos: {soma_positivos}")
print(f"Quantidade de números negativos: {qtd_negativos}")
print(f"Vetor com os números negativos: {negativos}")