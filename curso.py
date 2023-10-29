import random
import string


class Curso():

    contrasenias = {}
    __prox_codigo = 0

    def __init__(self, nombre: str, contrasenia_matriculacion = None):
        self.__nombre = nombre
        self.__codigo = Curso.prox_codigo()
        self.__nombre_carrera = "Tecnicatura Universitaria en Programación"
        if contrasenia_matriculacion is None:
            if nombre in Curso.contrasenias:
                self.__contrasenia_matriculacion = Curso.contrasenias[nombre]
            else:
                nueva_contrasenia = Curso.generar_contrasenia()
                Curso.contrasenias[nombre] = nueva_contrasenia
                self.__contrasenia_matriculacion = nueva_contrasenia
        else:
            self.__contrasenia_matriculacion = contrasenia_matriculacion
        self.__archivos = []

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def codigo(self):
        return self.__codigo
    
    @classmethod
    def prox_codigo(cls):
        cls.__prox_codigo += 1
        return cls.__prox_codigo
        
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    @contrasenia_matriculacion.setter
    def contrasenia_matriculacion(self, nueva_contrasenia_matriculacion):
        self.__contrasenia_matriculacion = nueva_contrasenia_matriculacion

    @property
    def archivos(self):
        return self.__archivos
    
    @property
    def nombre_carrera(self):
        return self.__nombre_carrera
    @nombre_carrera.setter
    def nombre_carrera(self, nuevo_nombre_carrera):
        self.__nombre_carrera = nuevo_nombre_carrera

    def generar_contrasenia():
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(5))
        return cod

    def __str__(self):
       return f"DATOS CURSO:\nNombre: {self.nombre}\nCodigo: {self.codigo}\nContraseña: {self.contrasenia_matriculacion}"
    
    def nuevo_archivo(self, archivo: object):

        self.archivos.append(archivo)

    
    