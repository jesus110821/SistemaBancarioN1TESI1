class Banco:
    def __init__(self, numero, nome):
        self.__numero = numero
        self.__nome = nome
        self.__contas = []

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def remover_conta(self, conta):
        self.__contas.remove(conta)

    def buscar_conta(self, numero):
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def get_contas(self):
        return self.__contas

    def get_numero(self):
        return self.__numero

    def get_nome(self):
        return self.__nome
