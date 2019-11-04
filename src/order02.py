from operator import attrgetter

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>Código {self._codigo} Saldo {self._saldo}<<]"

    def __eq__(self, outro):
        if type(outro) != ContaSalario and not isinstance(outro, ContaSalario):
            return False

        return self._codigo == outro._codigo #and self._saldo == outro._saldo

def extrai_saldo(conta):
    return conta._saldo

idades = [15, 87, 32, 65, 56, 32, 49, 37]
nomes = ["Guilherme", "Daniela", "Paulo"]

print(sorted(nomes))

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in contas:
    print(conta)

print("\n")

for conta in sorted(contas, key=extrai_saldo):
    print(conta)

print("\n")

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)