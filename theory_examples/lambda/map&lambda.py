# EJEMPLO DE MAP CON LAMBDA

# Crear lista del 0 al 4
lista1 = [x for x in range(5)]

# Crear lista mapeando una función lambda que eleva cada elemento de lista1 al cuadrado
lista2 = list(map(lambda x: 2 ** x, lista1))

# Imprimiendo lista2
print(lista2)

# Bucle for que mapea una función lambda que multiplica cada elemento de lista2 por si mismo
for x in map(lambda x: x * x, lista2):
	print(x, end=' ')
print()