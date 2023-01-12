def ranges(char):
    return ["A", "Z"] if char.isupper() else ["a", "z"]


def displacement(number, char, limits):
    if char.isalpha() and isinstance(number, int):
        code = ord(char) + number if 1 <= number <= 25 else ord(char) + 1
        if code > ord(limits[1]):
            code -= ord(limits[1]) - ord(limits[0]) + 1

    else:
        code = ord(char)

    return code


def encipher(number, to_cipher):
    for index, char in enumerate(to_cipher):
        limit = ranges(char)
        code = displacement(number, char, limit)
        to_cipher[index] = chr(code)

    print("".join(to_cipher).replace("  ", " "))


try:
    # Text to encipher
    text = input("Ingresa el texto a cifrar (Válidos: Espacios y letras y letra con números): ")
    if text == "" or text.isnumeric() or "  " in text or text == " ":
        raise Exception("No debe contener solamente números o espacios en blanco")

    # Number of displacements
    number = input("Numero de desplazamiento (Default +1: press enter): ")
    number = 1 if not number.isnumeric() else int(number)

    # List whit characters to encipher
    to_cipher = [element for element in text]

    # encipher function
    encipher(number, to_cipher)

except ValueError as only_numbers:
    print("Error: intenta otra vez")

except Exception as only_text:
    print("Error", only_text)
