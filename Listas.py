from turtledemo.penrose import start


class Listas:
    def __init__(self, lista : list):
        if(lista == []):
            self.__Lista = []
        else:
            self.__Lista = lista

    def Extraer(self):
        return self.__Lista

    def Mostar(self):
        for c,x in enumerate(self.__Lista, start=1):
            print(f"{c}. {x}")


class LGenero(Listas):
    def __init__(self):
        __Genero = ["Hombre", "Mujer"]
        super().__init__(__Genero)

class LCategoria(Listas):
    def __init__(self):
        __Categorias = ["Tramite", "Actualizacion", "Registro"]
        super().__init__(__Categorias)

class LCategoriaOP1(Listas):
    def __init__(self):
        __Categorias1 = ["Nit", "RTU"]
        super().__init__(__Categorias1)

class LCategoriaOP2(Listas):
    class LCategoriaOP1(Listas):
        def __init__(self):
            __Categorias1 = ["Vheiculo", "Placas"]
            super().__init__(__Categorias1)


