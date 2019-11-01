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

class ContaSalarioHerda(ContaSalario):
    pass

conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

print(conta1 == conta2)

contas = [conta1]

print(conta1 in contas)
print(conta2 in contas)

conta3 = ContaSalarioHerda(37)

print(conta3 in contas)