

class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email
    
    @property
    def contrasenia(self):
        return self._contrasenia
    
    @contrasenia.setter
    def contrasenia(self, nuevo_contrasenia):
        self._contrasenia = nuevo_contrasenia

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nE-mail: {self.email}"

    def validar_credenciales(self, email_ingresado: str, contrasenia_ingresada: str):

        if (self.email == email_ingresado) & (self.contrasenia == contrasenia_ingresada):
            return True
        else:
            return False

