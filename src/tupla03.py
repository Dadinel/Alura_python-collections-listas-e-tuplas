class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}]<<".format(self.codigo, self.saldo)

guilherme = ("Guilherme", 37, 1981) #tupla
daniela = ("Daniela", 31, 1987)

usuarios = [guilherme, daniela]

usuarios.append(("Paulo", 39, 1979))

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)

conta_da_dani = ContaCorrente(234876)
conta_da_dani.deposita(1000)

contas = (conta_do_gui, conta_da_dani)

contas[0].deposita(300)