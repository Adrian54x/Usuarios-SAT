from Usuario import Usuarios
from datetime import datetime

class Idiomas:
    def __init__(self,dpi: int, nombres: str, apellidos: str, fechaDeNacimiento: datetime, genero: str, idioma: str):
        self.Idioma = idioma
        super().__init__ (self,dpi, nombres, apellidos, fechaDeNacimiento, genero)

    @property
    def Idioma(self):
        return self.__Idioma

    @Idioma.setter
    def Idioma(self, idioma:str):
        if len(str(idioma)) <=4:
            print("Idioma invalido")
        else:
            self.__Idioma = idioma

