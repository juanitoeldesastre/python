#Comentario
print("Hola mundo")
print(1 + 1)

#Definir y sa
nombre = "Juan"
print(f"Hola, soy {nombre} y tengo {10 + 10} años.")

#Lista de amigos
amigos = ["Mariana", "Karolg", "Scrappy"]
scooby = amigos[0]
dobidu = amigos[1]

print(scooby, dobidu)
print(f"Mi vida en otra realidad alterna es con {scooby} y en mi otra vida es con {dobidu}.")

#Tuplas
tupla = ("piedra", "caca", "chisito")
print(tupla)

mi_tupla = ('2', 'pinguino', '3.14')
mi_tupla = ('python',) + mi_tupla[1:3]
print(mi_tupla)

#Pokémon
poke = input("Ingrese un Pokémon para el laboratorio del Profesor Oak: ")

lista = ["Charmander", "Bulbasaur", "Squirtle"]
lista.append(poke)

print(f"Profesor Oak recibe un {poke} de regalo.")
print("Profesor Oak tiene estos Pokémon:", lista)
