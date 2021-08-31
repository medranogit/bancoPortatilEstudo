from time import sleep
class banco:
    def depositar(self, saldo, valor):

        new_saldo = saldo + valor
        print("\nSeu saldo atual é: ", new_saldo)

        sleep(1)
        return new_saldo


    def sacar(self, saldo, valor):
        new_saldo = saldo - valor
        

        trigger = True

        if new_saldo < 0:
            new_saldo = new_saldo + valor
            print("\n-------------------------------------\nVocê não tem saldo o suficiente")
            trigger = False
            sleep(1)
            
            return new_saldo

        if trigger == True:    
            print("\nSeu saldo atual é: ", new_saldo)
            sleep(1)
            return new_saldo

    