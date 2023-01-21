# EXAMPLE

pila = []


def push(val):
    pila.append(val)


def pop():
    try:
        val = pila[-1]
        del pila[-1]
        return val
    except IndexError:
        return "Empty stack"


def show():
    print(pila)


#======TEST=========
for _ in range(0, 10, 2):
    push(_)
show()

for _ in range(3):
    pop()
show()
