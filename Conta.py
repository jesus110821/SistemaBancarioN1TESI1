from datetime import datetime
from Cliente import Cliente

class Conta:
    def __init__(self, numero, titular, saldo):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__historico = []

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__historico.append((datetime.now(), 'Depósito', valor))
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and self.__saldo >= valor:
            self.__saldo -= valor
            self.__historico.append((datetime.now(), 'Saque', valor))
            return True
        return False

    def get_historico(self):
        return self.__historico

    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

# Classe ContaPoupanca
class ContaPoupanca(Conta):
    def __init__(self, numero, titular: Cliente, saldo=0.0, juros=0.02):
        super().__init__(numero, titular, saldo)
        self.juros = juros

    def atualizar_saldo(self):
        self.saldo += self.saldo * self.juros  # Aplica os juros no saldo

# Classe ContaCorrente
class ContaCorrente(Conta):
    def __init__(self, numero, titular: Cliente, saldo=0.0, desconto=1.0):
        super().__init__(numero, titular, saldo)
        self.desconto = desconto

    def sacar(self, valor):
        valor_total = valor + self.desconto  # Desconta o valor fixo no saque
        return super().sacar(valor_total)

    def depositar(self, valor):
        valor_total = valor - self.desconto  # Desconta o valor fixo no depósito
        super().depositar(valor_total)
