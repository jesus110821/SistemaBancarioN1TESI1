from datetime import datetime

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
