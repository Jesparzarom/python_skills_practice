def rangos(prompt: str, min: int, max: int) -> int:
    while True:
        try:
            entrada = int(input(prompt))
            assert (entrada >= min and entrada <= max)
            return entrada
        except ValueError: # Si el valor no es entero
            print(f"Error: entrada incorrecta")
        except AssertionError:  # Si el valor no está en el rango determinado
            print(f"Error: el valor no está dentro del rango {min} <--> {max}")


print(f"El número es {rangos('Ingrese número del -10 al 10 ► ', -10, 10)}")
