# Importar módulos a utilizar
from random import seed, randint

# Genera lista de números enteros del -10 al 10
seed()
data = [ randint(-10,10) for x in range(5) ]

# Lista con los datos filtrados con filter() mediante función lambda:
# --> números ( De < data >) que son pares y mayores que cero
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

# Impresiones
print(data)
print(filtered)