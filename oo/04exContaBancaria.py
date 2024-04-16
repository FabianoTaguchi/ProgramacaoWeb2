class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R${self.saldo}"

conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)
print(conta1)
print(conta2)


