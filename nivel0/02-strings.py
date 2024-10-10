nombre_valor = 'Hola mundo'
descripcion = """
Los detalles de este valor no son mas que imaginativos
ya que enrealidad no cuenta con detalles asi que los 
inventaremos jejeje 😀
"""
print(len(nombre_valor))
print(nombre_valor[0])
print(nombre_valor[0:10])
print(nombre_valor[:])
#se puede cambiar el primer valor 
nuevo_valor = 'h' + nombre_valor[1:]
print(f"Se cambiara el primer valor de 'Hola mundo' a {nuevo_valor}")
#ejemplos1s solo letras
cadena = "Solo letras en esta cadena"
print(f"La primera letra de la variable cadena es '{cadena[0]}' y la ultima es '{cadena[-1]}'") #primera letra y ultima letra 

#ejemplos2s [inicio:fin]
cadena = "Python es genial"
print(cadena[0:6])  #los primeros 6
print(cadena[7:])   #desde el índice 7 hasta el final
#operaciones adicionales
print(cadena.upper())  #convertir a mayúsculas
print(cadena.lower())  #convertir a minúsculas
print(cadena.replace("genial", "increíble"))  #reemplazar parte de la cadena
#print(cadena.strip())  #eliminar espacios en blanco
print(cadena.find("Python")) #buscar una subcadena
print(cadena.startswith("Python"))  # Verifica si la cadena empieza con "Python"
print(cadena.endswith("mondongo"))  #verifica si la cadena termina con "mondongo"

#operaciones con hola mundo
print("operaciones con hola mundo")
saludo = "Hola"
nombre = "mundo"
resultado = f"{saludo} {nombre}"
print(resultado)
#multiplicación
multi = "Hola mundo "
print(multi * 3)  #imprime 3 veces
#booleans
mensaje = "Hola mundo"
print("Hola" in mensaje)  #if hola in mensaje inprime True
print("Adios" in mensaje)    #if Adios in mensaje imprime False
#suma+string a int+string
sumando = "Agarra el ultimo numero 1"
numero = sumando.split()[-1]
sumita = int(numero)  # Convierte el string a un entero
#sumita = float(numero) 
print((sumita) + 1)  # 1+1
#ASCII
letra = "A"
ASCII = ord(letra)  #el valor ASCII de 'A' es 65
print(ASCII) 
