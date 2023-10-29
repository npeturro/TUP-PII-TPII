

class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, nuevo_email):
        self.__email = nuevo_email
    
    @property
    def contrasenia(self):
        return self.__contrasenia
    
    @contrasenia.setter
    def contrasenia(self, nuevo_contrasenia):
        self.__contrasenia = nuevo_contrasenia

    def __str__(self):
        print("DATOS USUARIO")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"E-mail: {self.email}")
        print("------------")

    def validar_credenciales(self, email_ingresado: str, contrasenia_ingresada: str):

        if (self.email == email_ingresado) & (self.contrasenia == contrasenia_ingresada):
            return True
        else:
            print("Usuario o contraseña incorrectos") 
            return False

