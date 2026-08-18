num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if (num1 > num2):
    print(f"o primeiro número {num1} é maior que o segundo número {num2}.")
elif(num2 > num1):
    print(f"O Segundo número {num2} é maior que o primeiro número {num1}.")
else:
    print(f"Os números {num1} e {num2} são iguais.")