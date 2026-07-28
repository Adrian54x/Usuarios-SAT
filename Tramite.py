import Listas

class Tramites:
    def __init__(self, categoria : str, tipo : str):
        self.Categorias = categoria
        self.Tipos = tipo

    @property
    def Categorias(self):
        return self.__categorias

    @Categorias.setter
    def Categorias(self, Categorias):
        if Categorias in Listas.LCategoria().Extraer():
            self.__categorias = Categorias

    @property
    def Tipos(self):
        return self.__tipos

    @Tipos.setter
    def Tipos(self, Tipos):
        self.__tipos = Tipos
