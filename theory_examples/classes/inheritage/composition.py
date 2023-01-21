# EXAMPLE

import time

class Pistas:
    def cambiardireccion(self, izquierda, on):
        print("pistas: ", izquierda, on)

class Ruedas:
    def cambiardireccion(self, izquierda, on):
        print("ruedas: ", izquierda, on)

class Vehiculo:
    def __init__(self, controlador):
        self.controlador = controlador

    def girar(self, izquierda):
        self.controlador.cambiardireccion(izquierda, True)
        time.sleep(0.25)
        self.controlador.cambiardireccion(izquierda, False)

conRuedas = Vehiculo(Ruedas()) # El controlador del giro son Ruedas
conPistas = Vehiculo(Pistas()) # El controlador del giro son Pistas de Oruga

conRuedas.girar(True) # Girar Izquierda True
conPistas.girar(False)# Girar Izquierda False