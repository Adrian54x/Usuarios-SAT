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

class LTipoOP1(Listas):
    def __init__(self):
        __Tipo1 = ["Nit", "RTU"]
        super().__init__(__Tipo1)

class LTipoOP2(Listas):
        def __init__(self):
            __Tipo2 = ["Vheiculo", "Placas"]
            super().__init__(__Tipo2)

class LTipoOP3(Listas):
    def __init__(self):
        __Tipo4 = ["Unico", "Varios"]
        super().__init__(__Tipo4)

class LTipoOP4(Listas):
    def __init__(self):
        __Tipo6 = ["caja 1", "caja 2", "caja 3", "caja 4", "caja 5"]
        super().__init__(__Tipo6)

class LCategoriaV(Listas):
    def __init__(self):
        __Vheiculo = ["Terrestre","Aereo","Acuatico"]
        super().__init__(__Vheiculo)

class LTipoV(Listas):
    def __init__(self):
        __TipoVheiculo = ["Particular","Comercial","Alquiler","Urbano","Diplomatico","Oficial","Motocicleta"]
        super().__init__(__TipoVheiculo)

class LCategoriaOP3(Listas):
    def __init__(self):
        __Categorias3 = ["pago", "multas", "impugnaciones"]
        super().__init__(__Categorias3)

class LCategoriaOP4(Listas):
    def __init__(self):
        __Categotia4 = ["Orientación", "agencia virtual"]
        super().__init__(__Categotia4)

class LCategoriaOP5(Listas):
    def __init__(self):
        __Categorias5 = ["Expediente", "Ventanilla"]
        super().__init__(__Categorias5)

class LTipoOP5(Listas):
    def __init__(self):
        __Tipo5 = ["Ventanilla 1", "Ventanilla 2"]
        super().__init__(__Tipo5)

class LContiente(Listas):
    def __init__(self):
        __Continentes = ["America","Europa","Asia","Africa","Oceania","Antartida"]
        super().__init__(__Continentes)



