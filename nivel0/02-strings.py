
nombre_valor = 'Hello word'
descripcion = """
Los detalles de este valor no son mas que imaginativos
ya que enrealidad no cuenta con detalles asi que los 
inventaremos 😀  
"""
print(len(nombre_valor))
print(nombre_valor[0])
print(nombre_valor[0:10])
print(nombre_valor[:])
#se puede sumar c:
nueva_valor = 'h' + nombre_valor[1:]
print(nueva_valor)
#ejemplos1s solo letras
cadena = "Solo letras en esta cadena"
print(cadena[0]) #primera letra
print(cadena[-1]) #ultima letra
#ejemplos2s [inicio:fin]
cadena = "Python es genial"
print(cadena[0:6])  #los primeros 6
print(cadena[7:])   #desde el índice 7 hasta el final

#operaciones con hola mundo
print("operaciones con hola mundo")
saludo = "Hola"
nombre = "Mundo"
resultado = saludo + " " + nombre
print(resultado)
#multiplicación
multi = "Hola mundo "
print(multi * 3)  #imprime 3 veces
#booleans
mensaje = "Hola mundo"
print("Hola" in mensaje)  #if hola in mensaje inprime True
print("Adios" in mensaje)    #if Adios in mensaje imprime False

