from datos import *
import os


print("\n¡Bienvenido!")
respuesta = ''

def menu():
    print("1 - Ingresar como alumno")
    print("2 - Ingresar como profesor")
    print("3 - Ver cursos")
    print("4 - Salir")

def menu_estudiante():
    print("1 - Matricularse a un curso")
    print("2 - Desmatricularse a un curso")
    print("3 - Ver cursos")
    print("4 - Volver al menú principal")

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
                    alumno_encontrado = True
                    if contrasenia_ingresada == alumno.contrasenia:
                        os.system ("cls")
                        print(f"\n¡Hola {alumno.nombre}!")
                        respuesta2 = ''
                        while respuesta2 != "salir":                            
                            menu_estudiante()
                            opt2 = input("\n Ingrese la opción de menú: ")
                            os.system ("cls")                       
                            #---MATRICULARSE A CURSO---#
                            try:
                                if int(opt2) == 1:
                                    for carrera in carreras:
                                        if alumno.carrera == carrera.nombre:
                                            cursos_ordenados_codigo = sorted(cursos, key=lambda curso: curso.codigo) #Ordenanda la lista por codigo de curso
                                            for curso in cursos_ordenados_codigo:
                                                print(f"{curso.codigo} - {curso.nombre}")
                                            opc3 = int(input("\nIngrese el codigo del curso al cual quiere matricularse: "))
                                            if opc3 <= len(cursos):
                                                #Guardando instancia de curso
                                                for curso in cursos:
                                                    if curso.codigo == opc3:
                                                        nombre_carrera = curso.nombre
                                                password = input(" Ingrese la contraseña del curso: ")
                                                lista_cursos = alumno.matricular_en_curso(nombre_carrera, password)
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
                                        else:
                                            print("Usted no se encuentra cursando la carrera en la que se dicta dicho curso")
                                            input("Presione enter para continuar..")
                                            os.system ("cls") 
                                                                                  
                                
                                    AlumnosMis_cursos = sorted(alumno.mis_cursos, key=lambda curso: curso, reverse=True)
                                    #---DESMATRICULARSE A CURSO---#
                                elif int(opt2) == 2:
                                    
                                    for indice, curso in enumerate(AlumnosMis_cursos, 1):
                                        print(f"{indice} - {curso}")
                                    opc3 = int(input("\n Ingrese el numero del curso al cual quiere desmatricularse: "))
                                    if opc3 <= len(AlumnosMis_cursos):
                                        curso = AlumnosMis_cursos[opc3-1]
                                        alumno.desmatricular_curso(curso)
                                        print("Desmatriculado exitosamente!")
                                        input("Presione enter para continuar..")
                                        os.system ("cls")
                                    else:
                                        print("Ingrese una opción válida")
                                        input("Presione enter para continuar..")
                                        os.system ("cls") 

                                    #---LISTA DE CURSOS DEL ALUMNO---#
                                elif int(opt2) == 3 :
                                    
                                    for indice, curso in enumerate(alumno.mis_cursos, 1):
                                        print(f"{indice} - {curso}")
                                        
                                    print("\nIngrese el número del curso si desea ver más detalles")
                                    opt4 = int(input("o 0 para salir: "))
                                    os.system("cls")
                                    if opt4 <= len(alumno.mis_cursos) and opt4 != 0:
                                        nombre = alumno.mis_cursos[opt4 - 1]
                                        for curso in cursos:  # Asegúrate de que "cursos" esté definido y contenga la información correcta
                                            if curso.nombre == nombre:
                                                archivos_curso = curso.archivos
                                                print("-------------")
                                                print(f"Nombre: {nombre}")
                                                for archivo in archivos_curso:
                                                    print(f"{archivo.__str__()}")
                                                print("-------------\n")

                                
                                elif int(opt2) == 4 :
                                    respuesta2 = "salir"
                                else:
                                    print("Ingrese una opción correcta")
                                    input("Presione enter para continuar..")
                            except:
                                print("Ingrese una opción válida")
                                input("Presione enter para continuar..")
                                os.system ("cls")
                    else:
                        print("Contraseña incorrecta")
            if not alumno_encontrado:            
                print("Email NO encontrado. Debe darse de alta en alumnado")
                      
        #---INGRESO DOCENTES---#        

        elif int(opt) == 2:
            email_ingresado = input("Ingrese su email: ")
            if email_ingresado == "admin":
                print("Ingrese los datos para darse de alta")
                print("--------------------")
                nombre = input("Ingrese su nombre: ")
                apellido = input("Ingrese su apellido: ")
                email = input("Ingrese su email: ")
                contraseña = input("Ingrese contraseña: ")
                titulo = input("Ingrese nombre del titulo: ")
                anio_egreso = input("Ingrese el año de egreso: ")
                nuevo_profesor = Profesor(nombre, apellido, email, contraseña, titulo, anio_egreso)
                profesores.append(nuevo_profesor)
                print("Su usuario fue dado de alta exitosamente!")

            else:
                contrasenia_ingresada = input("Ingrese su contraseña: ")
                docente_encontrado = False  # Variable para controlar si se encontró un docente

                for profesor in profesores:
                    if email_ingresado == profesor.email:
                        docente_encontrado = True
                        if contrasenia_ingresada == profesor.contrasenia:
                            os.system ("cls")
                            print(f"\n¡Hola {profesor.nombre}!")
                            respuesta2 = ''
                            while respuesta2 != "salir":
                                menu_profesor()
                                opt2 = input("\n Ingrese la opción de menú: ")
                                os.system ("cls")                                
                                #---CARGAR UN CURSO---#
                                try:
                                    if int(opt2) == 1:
                                        for indice, carrera in enumerate(carreras,1):
                                            print(f"{indice} - {carrera.nombre}")
                                        opc4 = int(input("\n Ingrese el número de carrera a la cual se le asignará la materia: "))
                                        if opc4 <= len(carreras):
                                            carrera_seleccionada = carreras[opc4-1]
                                        nuevo_curso = input(" Ingrese el nombre del curso: ").title()
                                        
                                        if nuevo_curso in profesor.mis_cursos:
                                                print("Ingrese un curso con distinto nombre")
                                                input("Presione enter para continuar..")
                                                os.system ("cls")
                                        
                                        elif nuevo_curso == (''):
                                            print("Debe ingresar un nombre")
                                            input("Presione enter para continuar..")
                                            os.system ("cls")                                            
                                            
                                        else:
                                            curso_ingresado = Curso(nuevo_curso)
                                            cursos.append(curso_ingresado)
                                            carrera_seleccionada.agregar_materias(curso_ingresado)
                                            profesor.dictar_curso(nuevo_curso)
                                            print("-----------------")
                                            print(curso_ingresado.__str__())
                                            print("-----------------")
                                            input("Presione enter para continuar..")
                                            os.system ("cls") 
                                        #---LISTA DE CURSOS DEL DOCENTE---#
                                    
                                        profesorMis_cursos = sorted(profesor.mis_cursos, key=lambda curso: curso, reverse=True)
                                    elif int(opt2) == 2:
                                        
                                        for indice, curso in enumerate(profesorMis_cursos, 1):
                                            print(f"{indice} - {curso}")
                                        print("\n Ingrese el número del curso si desea ver mas información: ")
                                        opt5 = int(input("o 0 para salir: "))
                                        if opt5 != 0:
                                            nombre = profesorMis_cursos[opt5-1]
                                            print("-------------")
                                            print(f"Nombre: {nombre}")
                                            for curso in cursos:
                                                if curso.nombre == nombre:
                                                    print(f"Codigo: {curso.codigo}")
                                                    print(f"Contraseña: {curso.contrasenia_matriculacion}")
                                                    numero_archivos = len(curso.archivos)
                                                    print(f"Cantidad de archivos: {numero_archivos}")
                                            print("-------------")
                                            respuesta3 = input("¿Desea agregar un archivo adjunto? (S/N): ").lower()
                                            if respuesta3 == "s":
                                                nombre_archivo = input("Ingrese el nombre del archivo: ")
                                                formato = input("Ingrese el formato del archivo: ")
                                                nuevo_archivo = Archivo(nombre_archivo, formato)
                                                for curso in cursos:
                                                    if curso.nombre == nombre:
                                                        curso.nuevo_archivo(nuevo_archivo)
                                                print("Archivo creado exitosamente!")
                                                input("Presione enter para continuar..")
                                                os.system ("cls") 
                                            else:
                                                input("Presione enter para continuar..")
                                                os.system ("cls") 
                                    elif int(opt2) == 3 :
                                        respuesta2 = "salir"
                                    else:
                                        print("Ingrese una opción correcta")
                                        input("Presione enter para continuar..")
                                        os.system ("cls")
                                except:
                                    print("Ingrese una opción válida")
                                    input("Presione enter para continuar..")
                                    os.system ("cls") 
                        else:
                            print("Contraseña incorrecta")

                if not docente_encontrado:
                    print("Email NO encontrado.")
        
        #---VER TODOS LOS CURSOS DE LA CARRERA---#
            
        elif int(opt) == 3:
            
            if not cursos:
                print("No se encuentran cursos cargados")
            else:
            
                cursos_ordenados = sorted(cursos, key=lambda curso: curso.nombre) #Ordenando alfabeticamente la lista por nombre de curso

                #Guardando la longitud máxima del nombre de la materia y la contraseña
                max_length_nombre = max(len(curso.nombre) for curso in cursos_ordenados)            

                for i, curso in enumerate(cursos_ordenados):
                    print("-" * 89)
                    # Alinea el nombre de la materia y la contraseña en columnas usando ljust()
                    print(f"Materia: {curso.nombre.ljust(max_length_nombre)} | Codigo: {curso.codigo} | Carrera: Tecnicatura Universitaria en Programación")

                    # Comprueba si es la última materia, agrega una ultima linea de guiones y deja un espacio antes de mostrar el menú
                    if i == len(cursos_ordenados) - 1:
                        print("-" * 89)
                        print()
            
        elif int(opt) == 4:
            respuesta = "salir"

        else: print("Ingrese una opción válida")

    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....")
    os.system ("cls")

print("Hasta luego!.")