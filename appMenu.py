from estudiante import *
from curso import *
import os

cursos = [
    Curso("POO"),
    Curso("LABO"),
    Curso("Estadisticas")
]

estudiantes = [
    Estudiante("Nicolas", "Rodriguez", "jordiENP@gmail.com", "ABC123!", "12345", "2023"),
    Estudiante("Juan", "Perez", "juan@gmail.com", "123", "ABC", "2022"),
    Estudiante("Pedro", "Ramirez", "pedrito@gmail.com", "1111", "4567", "2021")
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
                        
                        print(f"Hola {alumno.nombre}")
                        print("1 - Matricularse a un curso")
                        print("2 - Ver curso")
                        print("3 - Volver al menu principal")
                        opt2 = input("\n Ingrese la opción de menú: ")
                        if int(opt2) == 1:
                            for indice, curso in enumerate(cursos, 1):
                                print(f"{indice} - {curso.nombre}")
                            opc3 = input("\n Ingrese la opcion del curso al cual quiere matricularse: ")
                            if int(opc3) == 1:
                                curso = "POO"
                                lista_cursos = alumno.matricular_en_curso(curso)
                                print(f"Su lista de cursos es: {lista_cursos}")
                                
                                
                    else:
                        print("Contraseña incorrecta")
                        break
            else:
                print("Email NO encontrado. Debe darse de alta en alumnado")
                
            
            """ejemplo.matricular_en_curso(cursos)"""
        elif int(opt) == 2:
            pass
        elif int(opt) == 3:
            #veo la llista, selecciono un curso y me devuelve 
            pass
        elif int(opt) == 4:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....")

print("Hasta luego!.")