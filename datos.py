from estudiante import *
from curso import *
from profesor import *
from carrera import *
from archivo import *



carreras = [
    Carrera("Tecnicatura Universitaria en Programación", 2)
]

cursos = [
    Curso("Ingles I"),
    Curso("Ingles II"),
    Curso("Laboratorio I"),
    Curso("Laboratorio II"),
    Curso("Programación I"),
    Curso("Programación II")
]

carreras[0].agregar_materias(cursos[4])

estudiantes = [
    Estudiante("Nicolas", "Rodriguez", "prueba@gmail.com", "123", "12345", "2023"),
    Estudiante("Juan", "Perez", "juan@gmail.com", "123", "ABC", "2022"),
    Estudiante("Pedro", "Ramirez", "pedrito@gmail.com", "1111", "4567", "2021")
]

"""estudiantes[0].matricular_en_carrera(carreras[0])"""

profesores = [
    Profesor("Paula", "Molina", "prueba@gmail.com", "123", "Kinesiologia", "2006"),
    Profesor("Federico", "Sarasa", "fede@gmail.com", "125", "Nutricionista", "1997"),
    Profesor("Nicolas", "Peturro", "nico@gmail.com", "1111", "Analista en Sistemas", "2021"),
    Profesor("Jordi", "Gimbernat", "jordania@gmail.com", "2222", "Ingeniero en Sistemas", "2100"),
]

archivos = [
    Archivo("tpi", "pdf"),
    Archivo("Practica1", "pdf")
]

cursos[4].nuevo_archivo(archivos[0])
cursos[4].nuevo_archivo(archivos[1])