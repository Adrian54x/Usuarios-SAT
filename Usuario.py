class Usuarios:
    def __init__(self, dpi, nombres, apellidos, pais, fechaDeNacimiento, genero):
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