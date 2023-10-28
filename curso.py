import random
import string


class Curso():
    contrasenias = {}
    __prox_cod = 0
    
    def __init__(self, nombre: str, contrasenia_matriculacion = None):
        self.__nombre = nombre
        self.__codigo = Curso.get_prox_cod()
        if contrasenia_matriculacion is None:
            if nombre in Curso.contrasenias:
                self.__contrasenia_matriculacion = Curso.contrasenias[nombre]
            else:
                nueva_contrasenia = Curso.generar_contrasenia()
                Curso.contrasenias[nombre] = nueva_contrasenia
                self.__contrasenia_matriculacion = nueva_contrasenia
        else:
            self.__contrasenia_matriculacion = contrasenia_matriculacion
    
    @classmethod
    def get_prox_cod(cls):
        cls.__prox_cod += 1
        return cls.__prox_cod
    
    @property
    def codigo(self):
        return self.__codigo

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
       return f"Nombre: {self.nombre}\nContraseña: {self.contrasenia_matriculacion}"

    
    