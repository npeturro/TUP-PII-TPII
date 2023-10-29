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
                                    cursos_ordenados_codigo = sorted(cursos, key=lambda curso: curso.codigo) #Ordenanda la lista por codigo de curso
                                    for indice, curso in enumerate(cursos_ordenados_codigo, 1):
                                        print(f"{indice} - {curso.nombre}")
                                    opc3 = int(input("\n Ingrese el codigo del curso al cual quiere matricularse: "))
                                    if opc3 <= len(cursos):
                                        curso = curso.codigo[opc3] #Guardando instancia de curso
                                        nombre_carrera = curso.nombre #Guardando nombre de ese curso
                                        #VALIDANDO Q EL ALUMNO ESTE EN LA CARREA EN LA Q SE DICTA DICHO CURSO
                                        if nombre_carrera in alumno.carrera:
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
                                        else:
                                            print("Usted no se encuentra cursando la carrera en la que se dicta dicho curso")                                        
                                    else:
                                        print("Ingrese una opción válida")
                                        input("Presione enter para continuar..")
                                        os.system ("cls")

                                    #---DESMATRICULARSE A CURSO---#
                                elif int(opt2) == 2:
                                    cursos_ordenados = sorted(cursos, key=lambda curso: curso.nombre, reverse = True) #Ordenando alfabeticamente la lista por nombre de curso
                                    for indice, curso in enumerate(cursos_ordenados, 1):
                                        print(f"{indice} - {curso.nombre}")
                                    opc3 = int(input("\n Ingrese el numero del curso al cual quiere desmatricularse: "))
                                    if opc3 <= len(cursos):
                                        curso = cursos_ordenados[opc3-1]
                                        alumno.desmatricular_curso(curso)

                                    #---LISTA DE CURSOS DEL ALUMNO---#
                                elif int(opt2) == 3 :
                                    
                                    for indice, mis_cursos in enumerate(alumno.mis_cursos,1):
                                        print(f"{indice} - {mis_cursos}")   
                                    print("\n Ingrese el número del curso si desea ver más detalles")
                                    opt4 = int(input("o 0 para salir: "))
                                    if opt4 != 0:
                                        nombre = alumno.mis_cursos[opt4-1]
                                        print("-------------")
                                        print(f"Nombre: {nombre}")
                                        curso_seleccionado = cursos[nombre]
                                        for archivo in curso_seleccionado.archivos:
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
                                    for indice, carrera in enumerate(carreras,1):
                                        print(f"{indice} - {carrera.nombre}")
                                    opc4 = int(input("\n Ingrese el numero de carrera a la cual se le asignará la materia: "))
                                    if opc4 <= len(carreras):
                                        carrera_seleccionada = carreras[opc4-1]
                                    nuevo_curso = input("Ingrese el nombre del curso: ")
                                    print("\n-------------")
                                    curso_ingresado = Curso(nuevo_curso)
                                    cursos.append(curso_ingresado)
                                    carrera_seleccionada.agregar_materias(curso_ingresado)
                                    profesor.dictar_curso(nuevo_curso)
                                    curso_ingresado.__str__()
                                    #---LISTA DE CURSOS DEL DOCENTE---#
                                elif int(opt2) == 2:
                                    cursos_ordenados = sorted(profesor.mis_cursos, key=lambda curso: curso.nombre, reverse = True) #Ordenando alfabeticamente la lista por nombre de curso
                                    for indice, mis_cursos in enumerate(cursos_ordenados,1):
                                        print(f"{indice} - {mis_cursos}")
                                    print("\n Ingrese el número del curso si desea ver mas información: ")
                                    opt5 = int(input("o 0 para salir: "))
                                    if opt5 != 0:
                                        nombre = profesor.mis_cursos[opt5-1]
                                        print("-------------")
                                        print(f"Nombre: {nombre}")
                                        curso_seleccionado = cursos[nombre]
                                        print(f"Codigo: {curso_seleccionado.codigo}")
                                        print(f"Contraseña: {Curso.contrasenias[curso_seleccionado]}")
                                        numero_archivos = len(curso_seleccionado.archivos)
                                        print(f"Cantidad de archivos: {numero_archivos}")
                                        print("-------------")
                                        respuesta3 = input("¿Desea agregar un archivo adjunto? (S/N): ")
                                        if respuesta3 == "S":
                                            nombre = input("Ingrese el nombre del archivo: ")
                                            formato = input("Ingrese el formato del archivo: ")
                                            nuevo_archivo = Archivo(nombre, formato)
                                            curso_seleccionado.nuevo_archivo(nuevo_archivo)
                                            
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
                admin = input(" Email NO encontrado. Ingrese codigo admin para darse de alta: ")
                if admin == "admin":
                    nombre = input(" Ingrese su nombre: ")
                    apellido = input(" Ingrese su apellido: ")
                    email = input(" Ingrese su email: ")
                    contraseña = input(" Ingrese contraseña: ")
                    titulo = input(" Ingrese nombre del titulo: ")
                    anio_egreso = input(" Ingrese el año de egreso: ")
                    nuevo_profesor = Profesor(nombre, apellido, email, contraseña, titulo, anio_egreso)
                    profesores.append(nuevo_profesor)
        
        #---VER TODOS LOS CURSOS DE LA CARRERA---#
            
        elif int(opt) == 3:
            cursos_ordenados = sorted(cursos, key=lambda curso: curso.nombre) #Ordenando alfabeticamente la lista por nombre de curso

            #Guardando la longitud máxima del nombre de la materia y la contraseña
            max_length_nombre = max(len(curso.nombre) for curso in cursos_ordenados)
            max_length_contrasenia = max(len(curso.contrasenia_matriculacion) for curso in cursos_ordenados)

            for i, curso in enumerate(cursos_ordenados):
                print("-" * 97)
                # Alinea el nombre de la materia y la contraseña en columnas usando ljust()
                # La password a modo desarrollador, despues hay que sacarla
                print(f"Materia: {curso.nombre.ljust(max_length_nombre)} | Contraseña: {curso.contrasenia_matriculacion.ljust(max_length_contrasenia)} | Carrera: Tecnicatura Universitaria en Programación")

                # Comprueba si es la última materia, agrega una ultima linea de guiones y deja un espacio antes de mostrar el menú
                if i == len(cursos_ordenados) - 1:
                    print("-" * 97)
                    print()
            
        elif int(opt) == 4:
            respuesta = "salir"

        else: print("Ingrese una opción válida")

    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....")
    os.system ("cls")

print("Hasta luego!.")