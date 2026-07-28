from Usuario import Usuarios
from Tramite import Tramites
from datetime import datetime
import Tramite

class Persona(Usuarios, Tramites):
    def __init__(self,dpi: int, nombres: str, apellidos: str, fechaDeNacimiento: datetime, genero:str, categoria : str, tipo : str, prioridad : str):
        super().__init__(dpi = dpi, nombres = nombres, apellidos = apellidos,
                         fechaDeNacimiento = fechaDeNacimiento, genero = genero,
                         categoria = categoria, tipo = tipo)
        self.Pioridad = prioridad

    @property
    def Pioridad(self):
        return self.__pioridad

    @Pioridad.setter
    def Pioridad(self,tipo: str):
        self.__pioridad = tipo