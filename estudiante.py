from usuario import *
from curso import *

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo: int, anio_inscripcion_carrera: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__mis_cursos = []

    @property
    def legajo(self):
        return self.__legajo
    
    @legajo.setter
    def legajo(self, nuevo_legajo):
        self.__legajo = nuevo_legajo

    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, nuevo_anio_inscripcion_carrera):
        self.__anio_inscripcion_carrera = nuevo_anio_inscripcion_carrera

    @property
    def mis_cursos(self):
        return self.__mis_cursos
    
    def __str__(self):
        print("DATOS ESTUDIANTE")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"E-mail: {self.email}")
        print(f"Legajo: {self.legajo}")
        print(f"Año de inscripción: {self.anio_inscripcion_carrera}")
        print("------------")

    def matricular_en_curso(self, curso, password):

        for cursos in self.mis_cursos:
            if curso == cursos:
                '''return ", ".join(self.mis_cursos)'''
                return False
            
        if curso in Curso.contrasenias and password == Curso.contrasenias[curso]:
            self.mis_cursos.append(curso)
            return True
        else:
            return None
     
 


