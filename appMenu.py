from estudiante import *
from curso import *
from profesor import *
import os
#hacerlo como diccionario
cursos = [
    Curso("Ingles I"),
    Curso("Ingles II"),
    Curso("Laboratorio I"),
    Curso("Laboratorio II"),
    Curso("Programación I"),
    Curso("Programación II")
]
estudiantes = [
    Estudiante("Nicolas", "Rodriguez", "jordiENP@gmail.com", "ABC123!", "12345", "2023"),
    Estudiante("Juan", "Perez", "juan@gmail.com", "123", "ABC", "2022"),
    Estudiante("Pedro", "Ramirez", "pedrito@gmail.com", "1111", "4567", "2021")
]
profesores = [
    Profesor("Paula", "Molina", "a", "123", "Kinesiologia", "2006"),
    Profesor("Federico", "Sarasa", "fede@gmail.com", "125", "Nutricionista", "1997"),
    Profesor("Nicolas", "Peturro", "nico@gmail.com", "1111", "Analista en Sistemas", "2021"),
    Profesor("Jordi", "Gimbernat", "jordania@gmail.com", "2222", "Ingeniero en casi todo", "2100"),
]

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Ingresar como alumno")
    print("2 - Ingresar como profesor")
    print("3 - Ver cursos")
    print("4 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls")
    if opt.isnumeric():
        if int(opt) == 1:
            email_ingresado = input("Ingrese su email: ")
            contrasenia_ingresada = input("Ingrese su contraseña: ")
            for alumno in estudiantes:
                if email_ingresado == alumno.email:
                    if contrasenia_ingresada == alumno.contrasenia:
                        print(f"¡Hola {alumno.nombre}!")
                        print("1 - Matricularse a un curso")
                        print("2 - Ver cursos")
                        print("3 - Volver al menú principal")
                        opt2 = input("\n Ingrese la opción de menú: ")
                        if int(opt2) == 1:
                            for indice, curso in enumerate(cursos, 1):
                                print(f"{indice} - {curso.nombre}")
                            opc3 = input("\n Ingrese la opcion del curso al cual quiere matricularse: ")
                            if int(opc3) == 1:
                                curso = "Ingles I"
                                password = input("Ingrese la contraseña del curso: ")
                                lista_cursos = alumno.matricular_en_curso(curso, password)
                                if lista_cursos == True:
                                    print("Curso agregado con éxito!")
                                elif lista_cursos == False:
                                    print("Usted ya se encuentra matriculado/a en este curso")
                                else:
                                    print("Contraseña incorrecta")
                        elif int(opt2) == 2 :
                            pass     
                    else:
                        print("Contraseña incorrecta")
                        break
            else:
                print("Email NO encontrado. Debe darse de alta en alumnado")    
            
            """ejemplo.matricular_en_curso(cursos)"""
        elif int(opt) == 2:
            email_ingresado = input("Ingrese su email: ")
            contrasenia_ingresada = input("Ingrese su contraseña: ")
            for profesor in profesores:
                if email_ingresado == profesor.email:
                    if contrasenia_ingresada == profesor.contrasenia:
                        print(f"¡Hola {profesor.nombre}!")
                        print("1 - Dictar curso")
                        print("2 - Ver cursos")
                        print("3 - Volver al menú principal")
                        opt2 = input("\n Ingrese la opción de menú: ")
                        if int(opt2) == 1:
                            #se podria validar q no este el curso
                            nuevo_curso = input("Ingrese el nombre del curso: ")
                            curso_ingresado = Curso(nuevo_curso)
                            cursos.append(curso_ingresado)
                            profesor.dictar_curso(nuevo_curso)
                            curso_ingresado.__str__()
                        elif int(opt2) == 2:
                            for indice, mis_cursos in enumerate(profesor.mis_cursos,1):
                                print(f"{indice} - {mis_cursos}")   
                    else:
                        print("Contraseña incorrecta")
                        break
            else:
                print("Email NO encontrado. Debe darse de alta en alumnado")    
        elif int(opt) == 3:
            ej = Curso("Ingles I")
            ej2 = Curso("Ingles II")
            ej.__str__()
            ej2.__str__()
            
        elif int(opt) == 4:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....")

print("Hasta luego!.")