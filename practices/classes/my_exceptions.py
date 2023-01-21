class ExcepcionDatosAlumnos(Exception):
    def __init__(self, filename="ERROR", mensaje="PROGRAM"):
        self.filename = filename
        self.mensaje = mensaje
        Exception.__init__(self)
           
    def __str__(self):
        return ("\n=========|ERROR|=========>  "  
                +f"{self.mensaje} {self.filename}" 
                +"  <=========|Interrupcion Forzada|=========\n")


class LineaErronea(ExcepcionDatosAlumnos):
    def __init__(self, filename):
        self.filename = f"{filename}.txt"
        self.mensaje = "EL CONTENIDO ES INCORRECTO:"


class ArchivoVacio(ExcepcionDatosAlumnos):
    def __init__(self, filename):
        self.filename = f"{filename}.txt"
        self.mensaje = "ARCHIVO SIN CONTENIDO:"


class NoEncontrado(ExcepcionDatosAlumnos):
    def __init__(self, filename):
        if not filename:
            self.filename = f"{filename}.txt"
            self.mensaje = "NOMBRE NO INGRESADO:"
        
        else:
            self.filename = f"{filename}.txt"
            self.mensaje = "ARCHIVO NO ENCONTRADO:"
    
        