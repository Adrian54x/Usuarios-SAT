from Usuario import Usuarios
from Tramite import Tramites
from datetime import datetime

class Persona(Usuarios, Tramites):
    def __init__(self,dpi: int, nombres: str, apellidos: str, fechaDeNacimiento: datetime, genero : str, categoria : str, tipo : str, prioridad : str):
        Usuarios.__init__(self, dpi, nombres, apellidos,fechaDeNacimiento, genero)
        Tramites.__init__(self, categoria, tipo)
        self.Pioridad = prioridad

    @property
    def Pioridad(self):
        return self.__pioridad

    @Pioridad.setter
    def Pioridad(self,tipo: str):
        if(tipo.lower() == "si" or tipo.lower() == "no"):
            self.__pioridad = tipo
        else:
            print("Tipo no valido!")

    def Mostrar(self):
        print("No. de dpi: ", self.Dpi)