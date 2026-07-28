from Usuario import Usuarios
from Tramite import Tramites
import Listas
from datetime import datetime

class Vehiculos(Usuarios, Tramites):
    def __init__(self,dpi: int, nombres: str, apellidos: str, fechaDeNacimiento: datetime, genero:str, categoria : str, tipo : str, categoriaV : str, tipoV: str):
        Usuarios.__init__(self, dpi, nombres, apellidos, fechaDeNacimiento, genero)
        Tramites.__init__(self, categoria, tipo)
        self.CategoriasV = categoriaV
        self.TiposV = tipoV

    @property
    def CategoriaV(self):
        return self.__categorias

    @CategoriaV.setter
    def CategoriaV(self,categoria):
        if categoria not in Listas.LCategoriaV().Extraer():
            print("Error, no se ha ingresado una categoria valida")
        else:
            self.__categorias = categoria

    @property
    def TipoV(self):
        return self.__tipos

    @TipoV.setter
    def TipoV(self,tipo):
        if tipo not in Listas.LTipoV().Extraer():
            print("Error, no se ha ingresado un tipo valido de vehiculo")
        else:
            self.__tipos = tipo

    def Mostrar(self):
        print("No. de dpi: ", self.Dpi)