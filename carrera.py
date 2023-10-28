
class Carrera():
    def __init__(self, nombre: str,cant_años: int):
        self.__nombre = nombre
        self.__cant_años = cant_años

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def cant_años(self):
        return self.__cant_años
    
    @cant_años.setter
    def cant_años(self, nuevo_cant_años):
        self.__cant_años = nuevo_cant_años

    def __str__(self):
        return f"Nombre: {self.nombre}\nCantidad de años: {self.cant_años}"
    
    def get_cantidad_materias():
        #Hacer una lista y que vaya contando cuantos tiene o hacer una lista e ir agregando solamente?
        pass