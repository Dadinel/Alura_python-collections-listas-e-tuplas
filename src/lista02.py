idades = []

idades.append(15)

print(28 in idades)
print(15 in idades)

if 15 in idades:
    idades.remove(15)

idades.append(19)

idades.insert(20,0)

print(idades)

idades.append([27,19])

for elemento in idades:
    print(elemento)

idades = [20, 39, 18]

idades.extend([27,19])

print(idades)

for idade in idades:
    print(idade + 1)

idade_no_ano_que_vem = []

for idade in idades:
    idade_no_ano_que_vem.append(idade + 1)

print(idade_no_ano_que_vem)

idade_no_ano_que_vem = [(idade + 1) for idade in idades]

print(idade_no_ano_que_vem)

print( [(idade) for idade in idades if idade > 21] )

def proximo_ano(idade):
    return idade + 1

print( [ proximo_ano(idade) for idade in idades ] )