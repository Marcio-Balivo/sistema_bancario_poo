from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco, contas):
        self._endereco = endereco
        self._contas = contas
    
    def realizar_transacao(self, conta, transacao):
        pass

    def adicionar_conta(self, conta):
        pass

class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def __str__(self):
        return ", ".join([f"{chave[1:]}: {valor}" for chave, valor in self.__dict__.items()])

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._cliente = cliente
        self._historico = historico

    def saldo(self):
        return self._saldo or 0
    
    def nova_conta(self, cliente, numero):
        pass # return conta

    def sacar(self, valor):
        self._valor = valor
        pass # return bool

    def depositar(self, valor):
        self._valor = valor
        pass # return bool

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self.limite_saques = limite_saques

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        self._conta = conta

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        self._conta = conta

class Historico:
    def adicionar_transacao(self, transacao):
        self._transacao = transacao

