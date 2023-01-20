"""LA FUNCIÓN LAMBDA TIENE LA SIGUIENTE ESTRUCTURA:

lambda parametro_s: expresion

"""
# =================================================
# EJEMPLO SIN LAMBDA
def imprimirfuncion(args, fun):
    for x in args:
        print("f(", x, ")=", fun(x), sep="")


def poli(x):
    return 2 * x**2 - 4 * x + 2


imprimirfuncion([x for x in range(-2, 3)], poli)


# =================================================
# EJEMPLO CON LAMBDA
def imprimirfuncion(args, fun):
    for x in args:
        print("f(", x, ")=", fun(x), sep="")


# Llamada a la función que imprime una función Lambda. 
# Ësta remplaza "in-situ" a la función anterior poli(x) ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
imprimirfuncion([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2) 

#====================================================
