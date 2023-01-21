'''ITER AND NEXT IN A CLASS. EXAMPLE'''
class Fib:
	def __init__(self, nn):
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self):
		print("Fib iter")
		return self

	def __next__(self):
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

class Class:
	def __init__(self, n):
		self.__iter = Fib(n)

	def __iter__(self):
		print("Class iter")
		return self.__iter;

'''YIELD EXAMPLE'''
def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia # Uso de yield en lugar de return
        potencia *= 2


# Invocación en list comprehensions
t = [x for x in potenciasDe2(5)]
print("Comprensión de listas -->", t)

# Invocación en método list()
t2 = list(potenciasDe2(5))
print("Función list() -->", t2)

# Contexto creado por operador "in"
for i in range(20):
    if i in potenciasDe2(4):
        print(i)
    
    
''' EJEMPLO FIBONACCI CON YIELD'''
def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(Fib(10))

print(fibs)