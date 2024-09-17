class Cliente:
    def __init__(self, nome, endereco, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf

    def set_nome(self, nome):
        self.__nome = nome

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return getattr(self, '_Cliente__telefone', '')
