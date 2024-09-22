import os

# Contador de perritos
perritos = 1
while perritos <= 10:
    print(f"Contador de perritos por ahora son: {perritos}")
    perritos += 1

# ContarOS
directorio = 'nivel1'
archivos = os.listdir(directorio)
contar = len(archivos)

print(f"Número de archivos en la carpeta: {contar}")

for archivo in archivos:
    print(f"Contando el archivo: {archivo}")

# Contarfor
lista = [1, 2, 3]
for numero in lista:
    print(f"Contando número: {numero}")

# Información
pokedex = {
    'Numero': 83,
    'Nombre': 'Farfetch',
    'Tipo': ['Volador', 'Normal']
}
print(f"El Pokémon {pokedex['Nombre']} es tipo {', '.join(pokedex['Tipo'])}.")

# Si
hijos = int(input("Ingrese cuántos hijos tiene: "))
if hijos <= 0:
    print("No tengo hijos.")
elif hijos <= 5:
    print(f"Los {hijos} hijos que tengo son muy pocos e insuficientes.")
elif hijos < 15:
    print(f"Los {hijos} hijos que tengo no son suficientes.")
elif hijos == 15:
    print(f"Los {hijos} hijos que tengo son suficientes.")
else:
    print(f"Los {hijos} hijos que tengo son más que suficientes.")
