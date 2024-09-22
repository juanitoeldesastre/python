# Error
try:
    print(sdajopkfj)
except NameError as error:
    print("Error:", error)

# Error/0
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print("ERROR:", error)

# IndexError
try:
    lista = ["uwu", "awa", "iwi", "owo", "ewe"]
    print(lista[1])
except IndexError as error:
    print("ERROR:", error)

# Función
def sumita(n1, n2):
    return n1 + n2

resultadosuma = sumita(12, 5)
print("Resultado de la suma:", resultadosuma)

# Función + input
def sumar(a, b):
    return a + b

a = int(input("Ingresa un número para a: "))
b = int(input("Ingresa un número para b: "))
suma = sumar(a, b)
print("Suma:", suma)

# Función - input
def restar(x, y):
    return x - y

x = int(input("Ingresa un número para x: "))
y = int(input("Ingresa un número para y: "))
puesta = restar(x, y)
print("Resultado de la resta:", puesta)
