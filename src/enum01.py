idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])

enumerate(idades)

print(list(range(len(idades))))
print(list(enumerate(idades)))

for indice, idade in enumerate(idades):
    print(indice, idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for usuario in usuarios:
    print(usuario)

for nome, _, _ in usuarios:
    print(nome)