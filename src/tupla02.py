class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}]<<".format(self.codigo, self.saldo)

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

conta_do_gui = ContaCorrente(15)
conta_da_dani = ContaCorrente(47685)

contas = [conta_do_gui, conta_da_dani]

print(contas[0], contas[1])

deposita_para_todas(contas)

print(contas[0], contas[1])

contas.insert(0,76)

print(contas[0], contas[1], contas[2])

guilherme = ("Guilherme", 37, 1981) #tupla
daniela = ("Daniela", 31, 1987)

print(guilherme)
print(daniela)

conta_gui = (15, 1000)

def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

print(conta_gui)

print(deposita(conta_gui))