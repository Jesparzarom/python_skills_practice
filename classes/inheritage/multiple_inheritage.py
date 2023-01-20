# EXAMPLE

''' Superclases y subclases: 3 niveles.'''
class Nivel1:
    variable1 = 100
    def __init__(self):
        self.var1 = 101

    def fun1(self):
        return 102


class Nivel2(Nivel1):
    variable2 = 200
    def __init__(self):
        super().__init__()
        self.var2 = 201
    
    def fun2(self):
        return 202


class Nivel3(Nivel2):
    variable3 = 300
    def __init__(self):
        super().__init__()
        self.var3 = 301

    def fun3(self):
        return 302


obj = Nivel3()

print(obj.variable1, obj.var1, obj.fun1())
print(obj.variable2, obj.var2, obj.fun2())
print(obj.variable3, obj.var3, obj.fun3())




''' Una subclase de dos superclases'''
class SuperA:
    varA = 10
    def funA(self):
        return 11

class SuperB:
    varB = 20
    def funB(self):
        return 21

class Sub(SuperA, SuperB):
    pass

obj = Sub()

print(obj.varA, obj.funA())
print(obj.varB, obj.funB())


''' Herencia: prioridad con variables del mismo nombre '''
class Nivel1:
    var = 100
    def fun(self):
        return 101

class Nivel2:
    var = 200
    def fun(self):
        return 201

class Nivel3(Nivel2):
    pass

obj = Nivel3()

print(obj.var, obj.fun(), obj.var)

''' Reglas de herencia: Lectura:
primero en el objeto, luego la en superclase (de abajo a arriba)
si hay mas de una superclase, de izquiera a derecha (en los parámetros)'''
class Izquierda:
    var = "I"
    varIzquierda = "II"
    def fun(self):
        return "Izquierda"


class Derecha:
    var = "D"
    varDerecha = "DD"
    def fun(self):
        return "Derecha"

class Sub(Izquierda, Derecha):
    pass


obj = Sub()

print(obj.var, obj.varIzquierda, obj.varDerecha, obj.fun())