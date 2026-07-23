
class Usuarios:
    def __init__(self, dpi: int, nombres: str, apellidos: str, pais: str, fechaDeNacimiento: str, genero: str):
        self.DPI = dpi
        self.Nombres = nombres
        self.Apellidos = apellidos
        self.Pais = pais
        self.FechaDeNacimiento = fechaDeNacimiento
        self.Genero = genero

    @property
    def Dpi(self):
        return self.DPI

    @property
    def Nombres(self):
        return self.Nombres

    @property
    def Apellidos(self):
        return self.Apellidos

    @property
    def Pais(self):
        return self.Pais

    @property
    def FechaDeNacimiento(self):
        return self.FechaDeNacimiento

    @property
    def Genero(self):
        return self.Genero

    @Dpi.setter
    def Dpi(self, dpi: int):
        if len(str(dpi)) == 13 and dpi in [1,2,3,4,5,6,7,8,9,0]:
            self.DPI = dpi
        else:
            raise ValueError("DPI no valido!")

    @Nombres.setter
    #def Nombres(self, nombres: str):
