idades = [15, 87, 32, 65, 56, 32, 49, 37]

print(idades)
print("\n")

print(sorted(idades))
print(list(reversed(idades)))
print(sorted(idades, reverse=True))
print(list(reversed(sorted(idades))))

idades.sort()

print("\n")
print(idades)