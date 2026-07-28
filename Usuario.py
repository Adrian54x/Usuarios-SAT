from datetime import datetime
import Listas
import re

class Usuarios:
    def __init__(self, dpi: int, nombres: str, apellidos: str, fechaDeNacimiento: datetime, genero: str):
        self.Dpi = dpi
        self.Nombres = nombres
        self.Apellidos = apellidos
        self.FechaDeNacimiento = fechaDeNacimiento
        self.Genero = genero

    @property
    def Dpi(self):
        return self.__DPI

    @property
    def Nombres(self):
        return self.__Nombres

    @property
    def Apellidos(self):
        return self.__Apellidos

    @property
    def FechaDeNacimiento(self):
        return self.__FechaDeNacimiento

    @property
    def Genero(self):
        return self.__Genero

    @Dpi.setter
    def Dpi(self, dpi: int):
        if len(str(dpi)) == 13:
            self.__DPI = dpi
        else:
            print("DPI no valido!")

    @Nombres.setter
    def Nombres(self, nombres: str):
        caractersValidos = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+(?: [a-zA-ZáéíóúÁÉÍÓÚñÑ]+)+$"
        val1 = re.fullmatch(caractersValidos, nombres)
        if not nombres.startswith(" ") and val1 and len(nombres) < 7:
            self.__Nombres = nombres
        else:
            print("Nombres no validos!")

    @Apellidos.setter
    def Apellidos(self, apellidos: str):
        caractersValidos = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+(?: [a-zA-ZáéíóúÁÉÍÓÚñÑ]+)+$"
        val1 = re.fullmatch(caractersValidos, apellidos)
        if apellidos.startswith(" ") and val1 and len(apellidos) < 7:
            self.__Apellidos = apellidos
        else:
            print("Apellidos no validos!")

    @FechaDeNacimiento.setter
    def FechaDeNacimiento(self, fechaDeNacimiento: datetime):
        if (datetime.today().year - fechaDeNacimiento.year > 18) and (datetime.today().year - fechaDeNacimiento.year <= 100):
            self.__FechaDeNacimiento = fechaDeNacimiento
        else:
            print("Fecha de nacimiento no valido!")

    @Genero.setter
    def Genero(self, genero: str):
        if genero in Listas.LGenero().Extraer():
            self.__Genero = genero
        else:
            print("Genero no valido!")
