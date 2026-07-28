from Usuario import Usuarios
from Tramite import Tramites
from datetime import datetime

class Idiomas(Usuarios, Tramites):
    def __init__(self,dpi: int, nombres: str, apellidos: str, fechaDeNacimiento: datetime, genero:str,categoria : str, tipo : str, idioma: str):
        Usuarios.__init__(self, dpi, nombres, apellidos, fechaDeNacimiento, genero)
        Tramites.__init__(self, categoria, tipo)
        self.Idioma = idioma

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

