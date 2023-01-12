fecha = input("Ingresa la fecha formato DD/MM/AAAA o DDMMAAA(sin separaciones) :")


def number_of_life(_input):
    replaces = _input.replace("/", "")
    if (
        (len(replaces) == 8)
        and (replaces[0:2] <= "31")
        and (replaces[2:4] <= "12")
        and (replaces.isnumeric())
    ):
        fecha = sum([int(num) for num in replaces])
        fecha = sum([int(num) if len(str(fecha)) == 2 else fecha for num in str(fecha)])
        return f"Resultado: {fecha}"

    else:
        return "Formato incorrecto"


print(number_of_life(fecha))
