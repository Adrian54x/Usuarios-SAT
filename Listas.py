class Listas:
    def __init__(self, lista : list):
        if(lista == []):
            self.__Lista = []
        else:
            self.__Lista = lista

    def Extraer(self):
        return self.__Lista

class LGenero(Listas):
    def __init__(self):
        Genero = ["Hombre", "Mujer"]
        super().__init__(Genero)