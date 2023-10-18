import random
import string


class Curso():
    def __init__(self, nombre: str, contrasenia_matriculacion = None):
        self.__nombre = nombre
        if contrasenia_matriculacion == None:
            self.__contrasenia_matriculacion = Curso.generar_contrasenia()
        else:
            self.__contrasenia_matriculacion = contrasenia_matriculacion
        """self.__contrasenia_matriculacion = Curso.generar_contrasenia()""" 

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    @contrasenia_matriculacion.setter
    def contrasenia_matriculacion(self, nueva_contrasenia_matriculacion):
        self.__contrasenia_matriculacion = nueva_contrasenia_matriculacion

    def generar_contrasenia():
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(5))
        return cod

    def __str__(self):
       print("DATOS CURSO")
       print(f"Nombre: {self.nombre}")
       print(f"Contraseña: {self.contrasenia_matriculacion}")
       print("------------")

    
    