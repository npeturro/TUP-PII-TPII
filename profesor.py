from usuario import *

class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, titulo: str, anio_egreso: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = []

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    @property
    def anio_egreso(self):
        return self.__anio_egreso
    
    @anio_egreso.setter
    def anio_egreso(self, nuevo_anio_egreso):
        self.__anio_egreso = nuevo_anio_egreso

    @property
    def mis_cursos(self):
        return self.__mis_cursos
    
    def __str__(self):
        print("DATOS PROFESOR")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"E-mail: {self.email}")
        print(f"Título: {self.titulo}")
        print(f"Año de egreso: {self.anio_egreso}")
        print("------------")

    def dictar_curso(self, curso):
        self.mis_cursos.append(curso)