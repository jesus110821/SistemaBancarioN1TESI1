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

    def gerar_relatorio(self):
        nome_arquivo = f"extrato_conta_{self.__numero}.txt"
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f"Extrato da Conta: {self.__numero}\n")
            arquivo.write(f"Titular: {self.__titular.get_nome()}\n\n")
            arquivo.write("Data, Operação, Valor\n")

            for data, operacao, valor in self.__historico:
                data_formatada = data.strftime('%d/%m/%Y %H:%M:%S')
                arquivo.write(f"{data_formatada}, {operacao}, R${valor:.2f}\n")

            arquivo.write(f"\nSaldo Final: R${self.__saldo:.2f}\n")

        print(f"Relatório salvo como {nome_arquivo}")

class ContaPoupanca(Conta):
    def __init__(self, numero, titular: Cliente, saldo=0.0, juros=0.02):
        super().__init__(numero, titular, saldo)
        self.juros = juros

    def atualizar_saldo(self):
        self.saldo += self.saldo * self.juros

class ContaCorrente(Conta):
    def __init__(self, numero, titular: Cliente, saldo=0.0, desconto=1.0):
        super().__init__(numero, titular, saldo)
        self.desconto = desconto

    def sacar(self, valor):
        valor_total = valor + self.desconto
        return super().sacar(valor_total)

    def depositar(self, valor):
        valor_total = valor - self.desconto
        super().depositar(valor_total)