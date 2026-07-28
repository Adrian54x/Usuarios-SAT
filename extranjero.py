from Usuario import Usuarios
from Tramite import Tramites
from idiomas import Idiomas
from datetime import datetime
import Listas

class Extranjero(Usuarios, Tramites, Idiomas):
    def __init__(self,dpi:int, nombres:str, apellidos:str, fechaDeNacimiento:datetime , genero:str, categoria : str, tipo : str, idioma: str, pais:str, continente:str):
        Usuarios.__init__(self,dpi, nombres, apellidos, fechaDeNacimiento, genero)
        Tramites.__init__(self, categoria, tipo)
        Idiomas.__init__(self,idioma)
        self.Pais = pais
        self.Continente = continente


    @property
    def Pais(self):
        return self.__Pais
    @Pais.setter
    def Pais(self,pais:str):
        if len(pais)<=3:
            print("Pais no valido")
        else:
            self.__Pais = pais

    @property
    def Continente(self):
        return self.__Continente
    @Continente.setter
    def Continente(self,continente:str):
        if continente not in Listas.LContiente().Extraer():
            print("El continente ingresado no es valido")
        else:
            self.__Continente = continente


    def mostrar_extranjero(self):
        print("No. de dpi: ", self.Dpi)
        print("Nombres: ", self.Nombres)
        print("Apellidos: ", self.Apellidos)
        print("Fecha de nacimiento: ", self.FechaDeNacimiento)
        print("Genero: ", self.Genero)
        print("Pais de origen:", self.Pais)
        print("Continente: ",self.Continente)