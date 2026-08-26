import random, os,time

numero_secreto = random.randint(1,100)
tentativas = 0

while True:
    numero = int(input('Digite o Numero Secreto: '))
    tentativas +=1
    if(numero == numero_secreto):
        print(f'Parabens Você acertou o numero em {tentativas} tentativas!')
        break
    elif(numero_secreto>numero):
        print(f'O numero secreto é maior !! - {tentativas} tentativas')
        time.sleep(3)
        os.system('cls' or 'clear')
    else:
        print(f'O numero secreto é menor !! - {tentativas} tentativas')
        time.sleep(3)
        os.system('cls' or 'clear')