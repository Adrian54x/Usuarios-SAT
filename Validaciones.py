from datetime import datetime

class Validacion:

    def  ValInt(self, texto : str, error : str):
        while True:
            try:
                return int(input(texto))
            except:
                print(error)


    def Dpi(self):
        while True:
            dpi = self.ValInt("Ingrese su DPI:", "DPI no valido!")
            if len(str(dpi)) != 13:
                print("DPI incorrecto!")
            else:
                return dpi


    def Nombre(self):
        while True:
            nombre = input("Ingrese sus nombres:")
            if nombre.startswith(" ") or len(nombre) < 7 or not nombre.replace(" ", "").isalpha():
                print("Nombres no validos!")
            else:
                return nombre

    def Apellido(self):
        while True:
            apellido = input("Ingrese su apellidos:")
            if(apellido.startswith(" ") or len(apellido) < 7 or not apellido.replace(" ", "").isalpha()):
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
                    return fecha
            except:
                print("Fecha no valida!")

# Genero, Categoria, Tipo, Discapacidad,TipoVehiculo, Idioma, Nacionalidad
x = Validacion()
a = x.FechaNacimiento()