from Usuario import Usuarios
from Tramite import Tramites
from datetime import datetime

class Vehiculos(Usuarios, Tramites):
    def __init__(self,dpi: int, nombres: str, apellidos: str, fechaDeNacimiento: datetime, genero:str, categoria : str, tipo : str, categorias : str, tipos : str):
        Usuarios.__init__(self, dpi, nombres, apellidos, fechaDeNacimiento, genero)
        Tramites.__init__(self, categoria, tipo)
        self.Categorias = categorias
        self.Tipos = tipos

    @property
    def Categorias(self):
        return self.__categorias

    @Categorias.setter
    def Categorias(self,categoria):
        if categoria not in ["Terrestre","Aereo","Acuatico"]:
            print("Error, no se ha ingresado una categoria valida")
        else:
            self.__categorias = categoria

    @property
    def Tipos(self):
        return self.__tipos

    @Tipos.setter
    def Tipos(self,tipo):
        if tipo not in ["Particular","Comercial","Alquiler","Urbano","Diplomatico","Oficial","Motocicleta"]:
            print("Error, no se ha ingresado un tipo valido de vehiculo")
        else:
            self.__tipos = tipo

    def mostrar_vehiculo(self):
        print("La informacion del vehiculo es la siguiente:_ ")
        print("")
        print("Categoria del vehiculo:_ ",self.Categorias)
        print("")
        print("Tipo de vehiculo:_ ",self.Tipos)