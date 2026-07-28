import re
from datetime import datetime
import Listas

class Validacion:

    def  ValInt(self, texto : str, error : str):
        while True:
            try:
                return int(input(texto))
            except:
                print(error)

    def SiNo(self, texto : str):
        while True:
            val = input(texto)
            if val.lower() == "si":
                return True
            elif val.lower() == "no":
                return False
            else:
                print("Valor incorrecto!")


    def Dpi(self):
        while True:
            dpi = self.ValInt("Ingrese su DPI:", "DPI no valido!")
            if len(str(dpi)) != 13:
                print("DPI incorrecto!")
            else:
                return dpi


    def Nombre(self):
        caractersValidos = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+(?: [a-zA-ZáéíóúÁÉÍÓÚñÑ]+)+$"
        while True:
            nombre = input("Ingrese sus nombres:")
            val1 = not re.fullmatch(caractersValidos, nombre)
            if nombre.startswith(" ") or val1  or len(nombre) < 7 :
                print("Nombres no validos!")
            else:
                return nombre

    def Apellido(self):
        caractersValidos = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+(?: [a-zA-ZáéíóúÁÉÍÓÚñÑ]+)+$"
        while True:
            apellido = input("Ingrese su apellidos:")
            val1 = not re.fullmatch(caractersValidos, apellido)
            if apellido.startswith(" ") or val1 or len(apellido) < 7:
                print("Apellidos no validos!")
            else:
                return apellido

    def Pais(self):
        while True:
            pais = input("Ingrese su pais:")
            if len(pais) < 3:
                print("Pais no validos!")
            else:
                return pais
    def FechaNacimiento(self):
        while True:
            try:
                fecha = input("Ingrese su fecha de nacimiento:")
                years = datetime.today().year - datetime.strptime(fecha.strip(), "%d/%m/%Y").year
                if years < 18 or years > 110 or not datetime.strptime(fecha.strip(), "%d/%m/%Y"):
                    print("Fecha incorrecta!")
                else:
                    return datetime.strptime(fecha.strip(), "%d/%m/%Y")
            except:
                print("Fecha no valida!")

    def Genero(self):
        genero = Listas.LGenero().Extraer()
        while True:
            opcion = self.ValInt("Elija el genero(1.Hombre / 2.Mujer):", "Opcion no valida")
            if opcion == 1:
                return genero[0]
            elif opcion == 2:
                return genero[1]
            else:
                print("Genero no valido!")

    def Categoria(self):
        Listas.LCategoria().Mostar()
        categorias = Listas.LCategoria().Extraer()
        while True:
            opcion = self.ValInt("Elija una categoria:", "Categoria no valida!")
            if(opcion > 0 and opcion <= len(categorias)):
                return categorias[opcion - 1]
            else:
                print("Categoria no valida!")

    def Tipos(self, opcion : int):
        if opcion == 1:
            Listas.LCategoriaOP1().Mostar()
            tipo = Listas.LCategoriaOP1().Extraer()
        else:
            print("Tipo no valido!")
        while True:
            opcion = self.ValInt("Elija un tipo:", "Tipo no valida!")
            if (opcion > 0 and opcion <= len(tipo)):
                return tipo[opcion - 1]
            else:
                print("Tipo no valida!")

# Discapacidad,TipoVehiculo, Idioma, Naconalidad
#x = Validacion()
#a = x.Tipos(1)