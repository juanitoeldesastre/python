pokedex = {
    'Numero' : 83,
    'Nombre' : 'Farfetch',
    'Tipo'   : ['Volador', 'Normal']
}

print(f"El pokemon {pokedex['Nombre']} es tipo {pokedex['Tipo']}")

hijos = int(input("Ingrese cuantos hijos tiene:"))
if hijos <=0:
   print(f"No tengo hijos")
elif hijos <= 5:
   print(f"Los {hijos} hijos que tengo son muy pocos e insuficientes")
elif hijos < 15:
   print(f"Los {hijos} hijos que tengo no son suficientes")
elif hijos == 15:
   print(f"Los {hijos} hijos que tengo son suficientes")
elif hijos > 15 :
   print(f"Los {hijos} hijos que tengo son mas que suficientes")
else:
   print("error 404")


