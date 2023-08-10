class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor : int):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor : int):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
    def get_saldo(self):
        return self.saldo

conta_1 = ContaBancaria(10000)
conta_1.depositar(5000)
conta_1.sacar(8000)

print(f"A Laura comprou uma moto de R$ 8.000,00 e ficou com saldo de R$ {conta_1.get_saldo()},00")