idades = [39, 30, 27, 18]

print(type(idades))

print(len(idades))

print(idades[0])
print(idades[1])
print(idades[2])
print(idades[3])

idades.append(15)

print(idades)

print(idades[4])

for idade in idades:
    print(idade)

idades.remove(30)

idades.append(15)

idades.remove(15)
idades.remove(15)

print(idades)

idades.clear()