import os 
import time

class ordenador:
    def __init__(self, nombre_carpeta):
        self.nombre_carpeta = nombre_carpeta

    def crear_carpeta(self):
        os.mkdir(self.nombre_carpeta)

    def eliminar_carpeta(self):
        os.rmdir(self.nombre_carpeta)

juanitoelusuario = ordenador("carpetita")

juanitoelusuario.crear_carpeta()
time.sleep(4)
juanitoelusuario.eliminar_carpeta()