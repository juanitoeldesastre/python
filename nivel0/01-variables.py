#cadenas de texto, string
nombre = "variables"
#números de coma flotante & números enteros, float and integer
pi = 3.14159265358979323846
x = 2
y = 1
#python distingue entre mayúculas y minúsculas por lo que PI es un valor diferente
PI = "mondongo" 
#operaciones matemáticas
operación1 = pi - (x + y) 
operación2 = x - y
#las variable x y y no cambian. en su lugar, se crean nuevas variables: suma1 y resta1,
#que almacenan los resultados de sumar x e y, y restar pi a x.
print(f"El resultado de la primera operación es : {operación1} y el resultado de la segunda es : {operación2}")
#imprimimos los valores x e y para ver si han cambiado
print(f"Los valores de las variables {x} e {y} siguen siendo los mismos; no han cambiado.")
#ahora si cambiaremos el valor de las variables reasignando su valor
x = [2,"dos",1+1]
y = {
    "suma": 0.5+0.5,
    "resta": 11-10,
    "multiplicacion": 1*1,
    "division": 2/2
}
#los valores cambiaron por lista y diccionario, lists and dictionaries
print(f"Los valores de las variables x e y no siguen siendo los mismos; han cambiado.")
print(f"Nuevo valor de x: {x}")
print(f"Nuevo valor de y: {y}")

#otro ejemplo para cambiar el valor de una variable es agregar una operación en la misma variable
pi += 1
#a la variable pi se le suma reasigna un numero que seria la suma += 1 
print(pi)
print(PI)
#imprimimos pi y mondongo

#ejemplos de concadenación de strings
nombre += " con"
concadenación = nombre + " " + PI
print(f"este curso se llama {concadenación}")