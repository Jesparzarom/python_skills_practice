try:
    linea = input("Ingresa una línea de números, sepáralos con espacios: ")
    strings = sum([float(num) for num in linea.split(" ")])
    print(f"Result = {strings}")
except ValueError:
    print("ValueError: Entry not valid")
