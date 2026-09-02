try:
    num = int(input("Digite um número para ver a tabuada: "))

    print(f"Tabuada do {num}:")
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")
except ValueError:
    print("Por favor, digite um número válido.")