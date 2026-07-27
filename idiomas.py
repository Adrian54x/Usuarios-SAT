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

    def mostrar_persona(self):
        print("No. de dpi: ", self.Dpi)
        print("Nombres: ", self.Nombres)
        print("Apellidos: ", self.Apellidos)
        print("Fecha de nacimiento: ", self.FechaDeNacimiento)
        print("Genero: ", self.Genero)
        print("Idioma que habla la persona: ", self.Idioma)

