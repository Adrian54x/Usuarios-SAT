from Usuario import Usuarios
from datetime import datetime
from Listas import LGenero
class Extranjero(Usuarios):
    def __init__(self,dpi:int, nombres:str, apellidos:str, fechaDeNacimiento:datetime , genero:str, continente:str):
        super().__init__(dpi, nombres, apellidos,fechaDeNacimiento, genero)
        self.Continente = continente

    @property
    def Continente(self):
        return self.__Continente
    @Continente.setter
    def Continente(self,continente:str):
        if len(continente) >= 4:
            self.__Continente = continente
        else:
            print("Continente no valido")


    def mostrar_extranjero(self):
        print("No. de dpi: ", self.Dpi)
        print("Nombres: ", self.Nombres)
        print("Apellidos: ", self.Apellidos)
        print("Fecha de nacimiento: ", self.FechaDeNacimiento)
        print("Genero: ", self.Genero)
        print("Continente: ",self.Continente)

gringo = Extranjero(2136548970601,"James Harold","McCormik shnider",datetime(1995,6,12),"Hombre","Europa")

gringo.mostrar_extranjero()