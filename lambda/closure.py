
#EJEMPLO 1 Sin la función interna sin parametros
def exterior(par):
	loc = par
	def interior():
		return loc
	return interior

var = 1
fun = exterior(var)
print(fun())

#EJEMPLO 2 con parametros
def crearcierre(par):
	loc = par
	def potencia(p):
		return p ** loc
	return potencia

fsqr = crearcierre(2) # Elevacion al cuadrado
fcub = crearcierre(3) # Elevación al cubo
for i in range(5):
	print(i, fsqr(i), fcub(i))