
class Carrera():
    def __init__(self, nombre: str, cant_anios: int) -> None:
        self.__nombre = nombre
        self.__cant_anios = cant_anios
        self.__cant_materias = Carrera.get_cantidad_materias
        self.__materias = []

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def cant_anios(self):
        return self.__cant_anios
    
    @cant_anios.setter
    def cant_anios(self, nueva_cant_anios):
        self.__cant_anios = nueva_cant_anios

    @property
    def cant_materias(self):
        return self.__cant_materias
    
    @property
    def materias(self):
        return self.__materias
    
    def __str__(self):
       return f"DATOS CARRERA:\nNombre: {self.nombre}\nCantidad de años: {self.cant_anios}\nCantidad de materias: {self.cant_materias}"
    
    def get_cantidad_materias(self) -> int:
        
        self.cant_materias = len(self.materias)

    def agregar_materias(self, materia: object):

        self.materias.append(materia)



    

