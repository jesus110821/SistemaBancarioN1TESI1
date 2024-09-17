import tkinter as tk
from tkinter import messagebox
from Banco import Banco
from Conta import ContaPoupanca, ContaCorrente
from Cliente import Cliente

bancos = []
contas = []
clientes = []

class TelaPrincipal:
    def __init__(self, root):
        self.root = root
        root.title("Sistema Bancário")
        root.geometry("400x300")

        # Menu
        menu = tk.Menu(root)
        root.config(menu=menu)

        banco_menu = tk.Menu(menu)
        menu.add_cascade(label="Banco", menu=banco_menu)
        banco_menu.add_command(label="Cadastrar Banco", command=self.cadastrar_banco)
        banco_menu.add_command(label="Mostrar Bancos", command=self.mostrar_bancos)

        conta_menu = tk.Menu(menu)
        menu.add_cascade(label="Conta", menu=conta_menu)
        conta_menu.add_command(label="Cadastrar Conta", command=self.cadastrar_conta)
        conta_menu.add_command(label="Mostrar Contas", command=self.mostrar_contas)
        conta_menu.add_command(label="Sacar", command=self.sacar_conta)
        conta_menu.add_command(label="Depositar", command=self.depositar_conta)
        conta_menu.add_command(label="Encerrar Conta", command=self.encerrar_conta)
        conta_menu.add_command(label="Gerar Relatório", command=self.gerar_relatorio)

        cliente_menu = tk.Menu(menu)
        menu.add_cascade(label="Cliente", menu=cliente_menu)
        cliente_menu.add_command(label="Cadastrar Cliente", command=self.cadastrar_cliente)
        cliente_menu.add_command(label="Mostrar Clientes", command=self.mostrar_clientes)
        cliente_menu.add_command(label="Atualizar Cliente", command=self.atualizar_cliente)
        cliente_menu.add_command(label="Remover Cliente", command=self.remover_cliente)

    # Funções para Banco
    def cadastrar_banco(self):
        janela = tk.Toplevel(self.root)
        janela.title("Cadastrar Banco")
        janela.geometry("300x200")

        tk.Label(janela, text="Número do Banco:").pack(pady=5)
        numero_entry = tk.Entry(janela)
        numero_entry.pack(pady=5)

        tk.Label(janela, text="Nome do Banco:").pack(pady=5)
        nome_entry = tk.Entry(janela)
        nome_entry.pack(pady=5)

        tk.Button(janela, text="Cadastrar", command=lambda: self.adicionar_banco(
            numero_entry.get(), nome_entry.get()
        )).pack(pady=20)

    def adicionar_banco(self, numero, nome):
        banco = Banco(numero, nome)
        bancos.append(banco)
        messagebox.showinfo("Sucesso", "Banco cadastrado com sucesso!")

    def mostrar_bancos(self):
        if bancos:
            lista_bancos = "\n".join([f"Número: {banco.get_numero()}, Nome: {banco.get_nome()}" for banco in bancos])
            messagebox.showinfo("Bancos Cadastrados", lista_bancos)
        else:
            messagebox.showinfo("Bancos", "Nenhum banco cadastrado.")

    # Funções para Conta
    def cadastrar_conta(self):
        janela = tk.Toplevel(self.root)
        janela.title("Cadastrar Conta")
        janela.geometry("400x400")

        tk.Label(janela, text="Número da Conta:").pack(pady=5)
        numero_entry = tk.Entry(janela)
        numero_entry.pack(pady=5)

        tk.Label(janela, text="Nome do Titular:").pack(pady=5)
        titular_entry = tk.Entry(janela)
        titular_entry.pack(pady=5)

        tk.Label(janela, text="Saldo Inicial:").pack(pady=5)
        saldo_entry = tk.Entry(janela)
        saldo_entry.pack(pady=5)

        # Adicionando a escolha do tipo de conta
        tipo_conta_var = tk.StringVar(value="Poupança")
        tk.Label(janela, text="Tipo de Conta:").pack(pady=5)
        tk.Radiobutton(janela, text="Poupança", variable=tipo_conta_var, value="Poupança").pack()
        tk.Radiobutton(janela, text="Corrente", variable=tipo_conta_var, value="Corrente").pack()

        tk.Button(janela, text="Cadastrar", command=lambda: self.adicionar_conta(
            numero_entry.get(), titular_entry.get(), saldo_entry.get(), tipo_conta_var.get()
        )).pack(pady=20)

    # Função para adicionar conta com a nova lógica
    def adicionar_conta(self, numero, titular_nome, saldo, tipo_conta):
        titular = Cliente(titular_nome, "", "")

        if tipo_conta == "Poupança":
            conta = ContaPoupanca(numero, titular, float(saldo))
        else:
            conta = ContaCorrente(numero, titular, float(saldo))

        contas.append(conta)
        messagebox.showinfo("Sucesso", f"Conta {tipo_conta} cadastrada com sucesso!")

    def mostrar_contas(self):
        if contas:
            lista_contas = "\n".join([
                                         f"Número: {conta.get_numero()}, Titular: {conta.get_titular().get_nome()}, Saldo: {conta.get_saldo():.2f}"
                                         for conta in contas])
            messagebox.showinfo("Contas Cadastradas", lista_contas)
        else:
            messagebox.showinfo("Contas", "Nenhuma conta cadastrada.")

    def sacar_conta(self):
        janela = tk.Toplevel(self.root)
        janela.title("Saque em Conta")
        janela.geometry("300x300")

        tk.Label(janela, text="Número da Conta:").pack(pady=5)
        numero_entry = tk.Entry(janela)
        numero_entry.pack(pady=5)

        tk.Label(janela, text="Valor do Saque:").pack(pady=5)
        valor_entry = tk.Entry(janela)
        valor_entry.pack(pady=5)

        tk.Button(janela, text="Sacar", command=lambda: self.realizar_saque(
            numero_entry.get(), valor_entry.get()
        )).pack(pady=20)

    def realizar_saque(self, numero, valor):
        conta = self.buscar_conta(numero)
        if conta:
            valor = float(valor)
            if conta.sacar(valor):
                messagebox.showinfo("Sucesso", f"Saque realizado com sucesso. Novo saldo: {conta.get_saldo():.2f}")
            else:
                messagebox.showwarning("Erro", "Saldo insuficiente para saque.")
        else:
            messagebox.showwarning("Erro", "Conta não encontrada.")

    def buscar_conta(self, numero):
        for conta in contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def depositar_conta(self):
        janela = tk.Toplevel(self.root)
        janela.title("Depósito em Conta")
        janela.geometry("300x300")

        tk.Label(janela, text="Número da Conta:").pack(pady=5)
        numero_entry = tk.Entry(janela)
        numero_entry.pack(pady=5)

        tk.Label(janela, text="Valor do Depósito:").pack(pady=5)
        valor_entry = tk.Entry(janela)
        valor_entry.pack(pady=5)

        tk.Button(janela, text="Depositar", command=lambda: self.realizar_deposito(
            numero_entry.get(), valor_entry.get()
        )).pack(pady=20)

    def realizar_deposito(self, numero, valor):
        conta = self.buscar_conta(numero)
        if conta:
            valor = float(valor)
            conta.depositar(valor)
            messagebox.showinfo("Sucesso", f"Depósito realizado com sucesso. Novo saldo: {conta.get_saldo():.2f}")
        else:
            messagebox.showwarning("Erro", "Conta não encontrada.")

    def encerrar_conta(self):
        janela = tk.Toplevel(self.root)
        janela.title("Encerrar Conta")
        janela.geometry("300x200")

        tk.Label(janela, text="Número da Conta:").pack(pady=5)
        numero_entry = tk.Entry(janela)
        numero_entry.pack(pady=5)

        tk.Button(janela, text="Encerrar", command=lambda: self.realizar_encerramento(numero_entry.get())).pack(pady=20)

    def realizar_encerramento(self, numero):
        conta = self.buscar_conta(numero)
        if conta:
            if conta.get_saldo() == 0:
                contas.remove(conta)
                messagebox.showinfo("Sucesso", "Conta encerrada com sucesso!")
            else:
                messagebox.showwarning("Erro", "Conta não pode ser encerrada. O saldo deve ser zero.")
        else:
            messagebox.showwarning("Erro", "Conta não encontrada.")

    def gerar_relatorio(self):
        if contas:
            relatorio = "\n".join([
                f"Número: {conta.get_numero()}, Titular: {conta.get_titular().get_nome()}, Saldo: {conta.get_saldo():.2f}"
                for conta in contas])
            messagebox.showinfo("Relatório de Contas", relatorio)
        else:
            messagebox.showinfo("Relatório", "Nenhuma conta cadastrada.")

    # Funções para Cliente
    def cadastrar_cliente(self):
        janela = tk.Toplevel(self.root)
        janela.title("Cadastrar Cliente")
        janela.geometry("300x300")

        tk.Label(janela, text="Nome do Cliente:").pack(pady=5)
        nome_entry = tk.Entry(janela)
        nome_entry.pack(pady=5)

        tk.Label(janela, text="CPF do Cliente:").pack(pady=5)
        cpf_entry = tk.Entry(janela)
        cpf_entry.pack(pady=5)

        tk.Label(janela, text="Endereço do Cliente:").pack(pady=5)
        endereco_entry = tk.Entry(janela)
        endereco_entry.pack(pady=5)

        tk.Label(janela, text="Telefone do Cliente:").pack(pady=5)
        telefone_entry = tk.Entry(janela)
        telefone_entry.pack(pady=5)

        tk.Button(janela, text="Cadastrar", command=lambda: self.adicionar_cliente(
            nome_entry.get(), cpf_entry.get(), endereco_entry.get(), telefone_entry.get()
        )).pack(pady=20)

    def adicionar_cliente(self, nome, cpf, endereco, telefone):
        cliente = Cliente(nome, endereco, cpf)
        cliente.set_telefone(telefone)
        clientes.append(cliente)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

    def mostrar_clientes(self):
        if clientes:
            lista_clientes = "\n".join([f"Nome: {cliente.get_nome()}, CPF: {cliente.get_cpf()}, Telefone: {cliente.get_telefone()}" for cliente in clientes])
            messagebox.showinfo("Clientes Cadastrados", lista_clientes)
        else:
            messagebox.showinfo("Clientes", "Nenhum cliente cadastrado.")

    def atualizar_cliente(self):
        janela = tk.Toplevel(self.root)
        janela.title("Atualizar Cliente")
        janela.geometry("300x300")

        tk.Label(janela, text="Nome do Cliente:").pack(pady=5)
        nome_entry = tk.Entry(janela)
        nome_entry.pack(pady=5)

        tk.Label(janela, text="Novo CPF:").pack(pady=5)
        cpf_entry = tk.Entry(janela)
        cpf_entry.pack(pady=5)

        tk.Label(janela, text="Novo Telefone:").pack(pady=5)
        telefone_entry = tk.Entry(janela)
        telefone_entry.pack(pady=5)

        tk.Button(janela, text="Atualizar", command=lambda: self.realizar_atualizacao(
            nome_entry.get(), cpf_entry.get(), telefone_entry.get()
        )).pack(pady=20)

    def realizar_atualizacao(self, nome, cpf, telefone):
        cliente = next((c for c in clientes if c.get_nome() == nome), None)
        if cliente:
            cliente.set_cpf(cpf)
            cliente.set_telefone(telefone)
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Cliente não encontrado.")

    def remover_cliente(self):
        janela = tk.Toplevel(self.root)
        janela.title("Remover Cliente")
        janela.geometry("300x200")

        tk.Label(janela, text="Nome do Cliente:").pack(pady=5)
        nome_entry = tk.Entry(janela)
        nome_entry.pack(pady=5)

        tk.Button(janela, text="Remover", command=lambda: self.realizar_remocao(nome_entry.get())).pack(pady=20)

    def realizar_remocao(self, nome):
        cliente = next((c for c in clientes if c.get_nome() == nome), None)
        if cliente:
            clientes.remove(cliente)
            messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")
        else:
            messagebox.showwarning("Erro", "Cliente não encontrado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaPrincipal(root)
    root.mainloop()
