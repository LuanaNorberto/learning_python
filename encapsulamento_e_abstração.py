# Encapsulamento

class ContaBancária:
    def __init__(self,saldo):
        self.__saldo = saldo



    def depositar(self,quantia):
        self.__saldo += quantia



    def obter_saldo(self):
        return self.__saldo
    
conta = ContaBancária(1000)
conta.depositar(500)
print(conta.obter_saldo())

# criei uma classe que é a conta bancária.
# defini o saldo e quantia/depósito.
# defini um resultado final com o obter saldo.
# a impressão é o valor da conta + a quantia de depósito, por fim, pedi o saldo total da classe = conta.