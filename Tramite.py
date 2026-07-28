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
        if Categorias in Listas.LCategoria().Extraer() or Categorias in Listas.LCategoriaOP3().Extraer():
            self.__categorias = Categorias

    @property
    def Tipos(self):
        return self.__tipos

    @Tipos.setter
    def Tipos(self, Tipos):
        val1 = Listas.LTipoV().Extraer()
        val2 = Listas.LTipoOP1().Extraer()
        val3 = Listas.LTipoOP2().Extraer()
        val4 = Listas.LTipoOP4().Extraer()
        val5 = Listas.LTipoOP5().Extraer()
        if Tipos in val1 or Tipos in val2  or Tipos in val3 or Tipos in val4 or Tipos in val5:
            self.__tipos = Tipos
        else:
            print("Tipo no valido")
