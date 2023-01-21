import functionss as notes
import my_exceptions as errors

try:
    FILENAME = "notes"
    try:
        notes.show_results(FILENAME)
    except errors.ArchivoVacio as e:
        print(e)
    except errors.LineaErronea as e:
        print(e)
    except errors.NoEncontrado as e:
        print(e)
except Exception as e:
    print(errors.ExcepcionDatosAlumnos())
    print("PROGRAM ERROR:", e, "\n")


