try:
    print(sdajopkfj)
except:
    print("Error")

try:
    10/0
except ZeroDivisionError as error:
    print("ERROR", error)


try:
    lista=["uwu","awa","iwi","owo","ewe"]
    print(lista[1])
except IndexError as error:
    print("ERROR", error)

def sumita(n1,n2):
 return n1+n2
resultadosuma = sumita(12,5)
print(resultadosuma)


def sumar(a,b):
 return a+b
a=(int(input("Ingresa un numero para a: ")))
b=(int(input("Ingresa un numero para b: ")))
suma = a+b
print(suma)

def restar(x,y):
 puesta = x - y
 return puesta

x=(int(input("Ingresa un numero para x: ")))
y=(int(input("Ingresa un numero para y: ")))
puesta = restar(x,y)
print(puesta)

