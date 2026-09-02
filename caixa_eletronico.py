try:
    saldo = float(input("Digite o saldo da conta: "))
    saque = float(input("Digite o valor do saque: "))
    if saque > saldo:
        print("Saldo insuficiente para realizar o saque.")
    else:
        saldo -= saque
        print(f"Saque realizado com sucesso. Saldo atual: {saldo:.2f}")
except ValueError:
    print("Por favor, digite valores válidos para saldo e saque.")