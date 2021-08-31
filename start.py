from time import sleep
from sistemas import banco

saldo = 0
#FALTA COLOCAR BANCO DE DADOS
while(True):

    bank = banco()

    pergunta = input("\n-------------------------------------\n- Bem vindo ao banco Brasilos\n- Digite o número da opção que deseja\n1 - Saldo \n2 - Depositar \n3 - Sacar \n4 - Sair \n-------------------------------------\n")
    if pergunta == "1":
        sleep(1)
        print("\nSeu saldo atual é: ", saldo )
        sleep(1)
        
    elif pergunta == "2":
        sleep(1)
        valorDeposito = int(input("Valor do deposito: "))
        saldo = bank.depositar(saldo, valorDeposito)

    elif pergunta == "3":
        sleep(1)
        valorSaque = int(input("Valor do saque: "))
        saldo = bank.sacar(saldo, valorSaque)
        
    elif pergunta == "4":
        break

    else:
        print("\n-------------------------------------\nSelecione um dos numeros")
    


