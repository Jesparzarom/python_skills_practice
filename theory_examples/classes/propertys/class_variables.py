# EXAMPLE

class ClaseEjemplo:
    contador = 0 # Class Variable
    def __init__(self, val = 1):
        self.__primera = val
        ClaseEjemplo.contador += 1

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo2 = ClaseEjemplo(4)

contador = objetoEjemplo1.contador
print(contador)


# Manejo de atributos condicionales dentro de la clase
class ClaseEjemplo2:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 2

objeto2 = ClaseEjemplo2(2)

# hasattr(*args, **kwargs)
if hasattr(objeto2, 'a'):
    print(objeto2.a)
else:
    print(objeto2.b)
    
    print("==============================")



# LLamando a los métodos
class conClase:
    varia = 2
    def metodo(self):
        print(self.varia, self.var)

obj = conClase()
obj.var = 3
obj.metodo()


print("==============================")


class conClase2():
    def otro(self):
        print("otro")

    def metodo(self):
        print("método")
        self.otro()

obj = conClase2()
obj.metodo()


print("==============================")