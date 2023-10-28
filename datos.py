from estudiante import *
from curso import *
from profesor import *

cursos = [
    Curso("Ingles I"),
    Curso("Ingles II"),
    Curso("Laboratorio I"),
    Curso("Laboratorio II"),
    Curso("Programación I"),
    Curso("Programación II")
]

estudiantes = [
    Estudiante("Nicolas", "Rodriguez", "a", "123", "12345", "2023"),
    Estudiante("Juan", "Perez", "juan@gmail.com", "123", "ABC", "2022"),
    Estudiante("Pedro", "Ramirez", "pedrito@gmail.com", "1111", "4567", "2021")
]

profesores = [
    Profesor("Paula", "Molina", "a", "123", "Kinesiologia", "2006"),
    Profesor("Federico", "Sarasa", "fede@gmail.com", "125", "Nutricionista", "1997"),
    Profesor("Nicolas", "Peturro", "nico@gmail.com", "1111", "Analista en Sistemas", "2021"),
    Profesor("Jordi", "Gimbernat", "jordania@gmail.com", "2222", "Ingeniero en casi todo", "2100"),
]
