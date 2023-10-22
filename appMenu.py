from estudiante import *
from curso import *
from profesor import *
import os

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

print("\n¡Bienvenido!")
respuesta = ''

def menu():
    print("1 - Ingresar como alumno")
    print("2 - Ingresar como profesor")
    print("3 - Ver cursos")
    print("4 - Salir")

def menu_estudiante():
    print("1 - Matricularse a un curso")
    print("2 - Ver cursos")
    print("3 - Volver al menú principal")

def menu_profesor():
    print("1 - Dictar curso")
    print("2 - Ver cursos")
    print("3 - Volver al menú principal")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls")
    if opt.isnumeric():
        
        #---INGRESO ALUMNOS---#
        
        if int(opt) == 1:
            email_ingresado = input("Ingrese su email: ")
            contrasenia_ingresada = input("Ingrese su contraseña: ")
            alumno_encontrado = False  # Variable para controlar si se encontró un alumno

            for alumno in estudiantes:
                if email_ingresado == alumno.email:
                    if contrasenia_ingresada == alumno.contrasenia:
                        os.system ("cls")
                        print(f"\n¡Hola {alumno.nombre}!")
                        respuesta2 = ''
                        alumno_encontrado = True
                        while respuesta2 != "salir":                            
                            menu_estudiante()
                            opt2 = input("\n Ingrese la opción de menú: ")
                            os.system ("cls")                       
                            #---MATRICULARSE A CURSO---#
                            try:
                                if int(opt2) == 1:
                                    for indice, curso in enumerate(cursos, 1):
                                        print(f"{indice} - {curso.nombre}")
                                    opc3 = int(input("\n Ingrese la opcion del curso al cual quiere matricularse: "))
                                    if opc3 <= len(cursos):
                                        nombre = cursos[opc3-1].nombre
                                        password = input(" Ingrese la contraseña del curso: ")
                                        lista_cursos = alumno.matricular_en_curso(nombre, password)
                                        if lista_cursos == True:
                                            print("-" * 25)
                                            print("Curso agregado con éxito!")
                                            print("-" * 25)
                                        elif lista_cursos == False:
                                            print("-" * 49)
                                            print("Usted ya se encuentra matriculado/a en este curso")                                       
                                            print("-" * 49)                                       
                                        else:
                                            print("-" * 22)
                                            print("Contraseña incorrecta")
                                            print("-" * 22)
                                        input("Presione enter para continuar..")
                                        os.system ("cls") 
                                    else:
                                        print("Ingrese una opción válida")
                                        input("Presione enter para continuar..")
                                        os.system ("cls")
                                                            
                                    #---LISTA DE CURSOS DEL ALUMNO---#
                                elif int(opt2) == 2 :
                                    
                                    for indice, mis_cursos in enumerate(alumno.mis_cursos,1):
                                        print(f"{indice} - {mis_cursos}")   
                                    print("\n Ingrese el número del curso si desea ver más detalles")
                                    opt4 = int(input("o 0 para salir: "))
                                    os.system ("cls")
                                    if opt4 != 0:
                                        nombre = alumno.mis_cursos[opt4-1]
                                        print("-------------")
                                        print(f"Nombre: {nombre}")
                                        print("-------------\n")
                                        
                                elif int(opt2) == 3 :
                                    respuesta2 = "salir"
                                else:
                                    print("Ingrese una opción correcta")
                                    input("Presione enter para continuar..")
                            except:
                                print("Ingrese una opción válida")
                                input("Presione enter para continuar..")             
                    else:
                        print("Contraseña incorrecta")
            if not alumno_encontrado:            
                print("Email NO encontrado. Debe darse de alta en alumnado")
                      
        #---INGRESO DOCENTES---#        

        elif int(opt) == 2:
            email_ingresado = input("Ingrese su email: ")
            contrasenia_ingresada = input("Ingrese su contraseña: ")
            docente_encontrado = False  # Variable para controlar si se encontró un docente

            for profesor in profesores:
                if email_ingresado == profesor.email:
                    if contrasenia_ingresada == profesor.contrasenia:
                        os.system ("cls")
                        print(f"\n¡Hola {profesor.nombre}!")
                        respuesta2 = ''
                        docente_encontrado = True
                        while respuesta2 != "salir":
                            menu_profesor()
                            opt2 = input("\n Ingrese la opción de menú: ")
                            os.system ("cls")                                
                            #---CARGAR UN CURSO---#
                            try:
                                if int(opt2) == 1:
                                    #Se podria validar que no este el curso
                                    nuevo_curso = input("Ingrese el nombre del curso: ")
                                    if nuevo_curso in profesor.mis_cursos:
                                        print("Ingrese un curso con distinto nombre")
                                        input("Presione enter para continuar..")
                                        os.system ("cls")
                                    else:
                                        print("\n-------------")
                                        curso_ingresado = Curso(nuevo_curso)
                                        cursos.append(curso_ingresado)
                                        profesor.dictar_curso(nuevo_curso)
                                        print("DATOS CURSO")
                                        curso_ingresado.__str__()
                                        print("------------\n")
                                    #---LISTA DE CURSOS DEL DOCENTE---#
                                elif int(opt2) == 2:
                                    for indice, mis_cursos in enumerate(profesor.mis_cursos,1):
                                        print(f"{indice} - {mis_cursos}")
                                    print("\n Ingrese el número del curso si desea ver la contraseña: ")
                                    opt3 = int(input("o 0 para salir: "))
                                    if opt3 != 0:
                                        nombre = profesor.mis_cursos[opt3-1]
                                        print("-------------")
                                        print(f"Nombre: {nombre}")
                                        print(f"Contraseña: {Curso.contrasenias[nombre]}")
                                        print("-------------")
                                        input("Presione enter para continuar..")
                                        os.system ("cls")
                                elif int(opt2) == 3 :
                                    respuesta2 = "salir"
                                else:
                                    print("Ingrese una opción correcta")
                                    input("Presione enter para continuar..")
                            except:
                                print("Ingrese una opción válida")
                                input("Presione enter para continuar..")
                    else:
                        print("Contraseña incorrecta")
            if not docente_encontrado:            
                print("Email NO encontrado. Debe darse de alta en alumnado")
        
        #---VER TODOS LOS CURSOS DE LA CARRERA---#
            
        elif int(opt) == 3:
            cursos_ordenados = sorted(cursos, key=lambda curso: curso.nombre) #Ordenando alfabeticamente la lista por nombre de curso

            #Guardando la longitud máxima del nombre de la materia y la contraseña
            max_length_nombre = max(len(curso.nombre) for curso in cursos_ordenados)
            max_length_contrasenia = max(len(curso.contrasenia_matriculacion) for curso in cursos_ordenados)

            for i, curso in enumerate(cursos_ordenados):
                print("-" * 77)
                # Alinea el nombre de la materia y la contraseña en columnas usando ljust()
                # print(Contraseña: {curso.contrasenia_matriculacion}) Para saber la contraseña de las materias queda comentado!
                print(f"Materia: {curso.nombre.ljust(max_length_nombre)} | Carrera: Tecnicatura Universitaria en Programación")

                # Comprueba si es la última materia, agrega una ultima linea de guiones y deja un espacio antes de mostrar el menú
                if i == len(cursos_ordenados) - 1:
                    print("-" * 77)
                    print()
            
        elif int(opt) == 4:
            respuesta = "salir"

        else: print("Ingrese una opción válida")

    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....")
    os.system ("cls")

print("Hasta luego!.") 