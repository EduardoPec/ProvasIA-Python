class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__saldo = saldo
        self.__titular = titular
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Deposito no valor de R$ {valor} realizado com sucesso!")
        else:
            print("Informe um valor válido!")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque no valor de R$ {valor} realizado com sucesso!")
        else:
            print("Informe um valor válido ou que não exceda o saldo!")
    
    def exibir_saldo(self):
        print(f"O saldo atual da sua conta bancaria é: R$ {self.__saldo}")

    def get_saldo(self):
        return self.__saldo

conta = ContaBancaria("Eduardo", 500)
conta.exibir_saldo()
conta.depositar(100)
conta.exibir_saldo()
conta.sacar(50)
conta.exibir_saldo()







