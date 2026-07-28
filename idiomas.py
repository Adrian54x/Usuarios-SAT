class Idiomas:
    def __init__(self,idioma: str):
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


