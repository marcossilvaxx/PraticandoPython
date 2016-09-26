class ContaCorrente:
    def __init__(self):
        self.numeroConta = float(input("Informe o número da conta:\n"))
        self.nomedoCorrentista = str(input("Informe o nome do correntista:\n"))
        self.saldo = 0
        print("Construtor finalizado.")
    def alterarNome(self):
        self.nomedoCorrentista = str(input("Informe o novo nome do correntista:\n"))
        print("Nome alterado.")
    def depósito(self):
        depósito = eval(input("Informe o valor do depósito:\n"))
        self.saldo += depósito
        print("Depósito efetuado com sucesso.")
        print("Saldo atual:", self.saldo)
    def saque(self):
        saque = eval(input("Informe o valor do saque:\n"))
        self.saldo -= saque
        print("Saque efetuado com sucesso.")
        print("Saldo atual:", self.saldo)

conta1 = ContaCorrente()

conta1.alterarNome()
conta1.depósito()
conta1.saque()