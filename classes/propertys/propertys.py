# EXAMPLE

"""SOME CLASS PROPERTY'S"""
from dataclasses import dataclass, field

# __dict__
class conClase:
    varia = 1
    def __init__(self):
        self.var = 2

    def metodo(self):
        pass

    def __oculto(self):
        pass

obj = conClase()

print(obj.__dict__)
print(conClase.__dict__)



# __name__
class conClase:
    pass

print(conClase.__name__)
obj = conClase()
print(type(obj).__name__)



# __module__
class conClase:
    pass

print(conClase.__module__)
obj = conClase()
print(obj.__module__)



# __bases__
class SuperUno:
    pass

class SuperDos:
    pass

class Sub(SuperUno, SuperDos):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperUno)
printBases(SuperDos)
printBases(Sub)