num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = (input("Selecione uma das operações sendo +, -, /, ou *: "))

if operacao == '+':
    resultado = num1 + num2
    print(f"A soma é {num1} + {num2} =  {resultado}")


elif operacao == '-':
    resultado = num1 - num2
    print(f"A subtração é {num1} - {num2} =  {resultado}")


elif operacao == '*':
    resultado = num1 * num2
    print(f"A multiplicação é {num1} * {num2} =  {resultado}")


elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"A divisão é {num1} / {num2} =  {resultado}")
    else:
        print("Erro, não é possível dividir por zero.")

else:
    print("erro")

