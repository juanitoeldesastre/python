#definir persona
def persona():
    nombre = "Juanito"
    edad = 20
    altura = 1.75
    descripcion = "Hola, soy Juanito el desarrollador 😀"
    es_estudiante = True
    habilidades = ["Python", "Minecraft", "Pokemon"]

    #codificación utf-8 para las tildes y emojis
    with open("persona.txt", "w", encoding="utf-8") as file:
        file.write(f"Nombre: {nombre}\n")
        file.write(f"Edad: {edad}\n")
        file.write(f"Altura: {altura} metros\n")
        file.write(f"Descripción: {descripcion}\n")

        if es_estudiante:
            file.write("Juanito es estudiante.\n")
        else:
            file.write("Juanito no es estudiante.\n")

        file.write("Habilidades:\n")
        for habilidad in habilidades:
            file.write(f"- {habilidad}\n")

    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Altura: {altura} metros")
    print(f"Descripción: {descripcion}")

    if es_estudiante:
        print("Juanito es estudiante")
    else:
        print("Juanito no es estudiante")

    print("Habilidades:")
    for habilidad in habilidades:
        print(f"- {habilidad}")

persona()

