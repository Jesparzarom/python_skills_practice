# EXAMPLES


''' __str__ '''
class Super:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."

class Sub(Super):
    def __init__(self, nombre):
        Super.__init__(self, nombre)



# Sub hereda el método __str__ de la clase "Super"
# Esto le permite imprimir la frase entera como cadena, 
# sin poseer un método propio en la subclase. Llama a la función
# de super y la ejecuta.
obj = Sub("Andy")
print(obj)


''' super() '''
class Super:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."

class Sub(Super):
    def __init__(self, nombre):
        super().__init__(nombre)


obj = Sub("Andy")
print(obj)


''' variables de clase'''
# Probando propiedades: variables de clase
class Super:
    supVar = 1

class Sub(Super):
    subVar = 2

obj = Sub()

print(obj.subVar)
print(obj.supVar)


''' variables de instancia'''
# Probando propiedades: variables de instancia
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12

obj = Sub()

print(obj.subVar)
print(obj.supVar)

