import re
from datetime import datetime
import Listas
from Colas import Cola


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
            if opcion > 0 and opcion <= len(categorias):
                return categorias[opcion - 1]
            else:
                print("Categoria no valida!")

    def Tipos(self, opcion : int):
        if opcion == 1:
            Listas.LTipoOP1().Mostar()
            tipo = Listas.LTipoOP1().Extraer()
        elif opcion == 2:
            Listas.LTipoOP2().Mostar()
            tipo = Listas.LTipoOP2().Extraer()
        elif opcion == 3:
            Listas.LTipoOP3().Mostar()
            tipo = Listas.LTipoOP3().Extraer()
        elif opcion == 4:
            Listas.LTipoOP4().Mostar()
            tipo = Listas.LTipoOP4().Extraer()
        elif opcion == 5:
            Listas.LTipoOP5().Mostar()
            tipo = Listas.LTipoOP4().Extraer()
        else:
            print("Tipo no valido!")
        while True:
            opcion = self.ValInt("Elija un tipo:", "Tipo no valida!")
            if opcion > 0 and opcion <= len(tipo):
                return tipo[opcion - 1]
            else:
                print("Tipo no valida!")

    def CategoriaVehiculo(self):
        Listas.LCategoriaV().Mostar()
        categoria = Listas.LCategoriaV().Extraer()
        while True:
            opcion = self.ValInt("Elija un categoria:", "Categoria no valida!")
            if opcion > 0 and opcion <= len(categoria):
                return categoria[opcion - 1]
            else:
                print("Categoria no valida!")

    def TipoVehiculo(self):
        Listas.LTipoV().Mostar()
        categoria = Listas.LTipoV().Extraer()
        while True:
            opcion = self.ValInt("Elija un tipo:", "Tipo no valida!")
            if opcion > 0 and opcion <= len(categoria):
                return categoria[opcion - 1]
            else:
                print("Tipo no valida!")

    def CategoriaOP3(self):
        Listas.LCategoriaOP3().Mostar()
        categoria = Listas.LCategoriaOP3().Extraer()
        while True:
            opcion = self.ValInt("Elija una categoria:", "Categoria no valida!")
            if opcion > 0 and opcion <= len(categoria):
                return categoria[opcion - 1]
            else:
                print("Categoria no valida!")

    def CategoriaOP4(self):
        Listas.LTipoOP4().Mostar()
        categoria = Listas.LTipoOP4().Extraer()
        while True:
            opcion = self.ValInt("Elija una categoria:", "Categoria no valida!")
            if opcion > 0 and opcion <= len(categoria):
                return categoria[opcion - 1]
            else:
                print("Categoria no valida!")

    def CategoriaOP5(self):
        Listas.LTipoOP5().Mostar()
        categoria = Listas.LTipoOP5().Extraer()
        while True:
            opcion = self.ValInt("Elija una categoria:", "Categoria no valida!")
            if opcion > 0 and opcion <= len(categoria):
                return categoria[opcion - 1]
            else:
                print("Categoria no valida!")

    def Idioma(self):
        while True:
            idioma = input("Ingrese el nombre del Idioma: ")
            if len(idioma) < 4 and idioma.isdigit():
                print("Idioma no valio!")
            else:
                return idioma

    def Pais(self):
        while True:
            pais = input("Ingrese el nombre del Pais: ")
            if(len(pais) < 3 and pais.isdigit()):
                print("Pais no valida!")
            else:
                return pais

    def Continente(self):
        Listas.LContiente().Mostar()
        categoria = Listas.LContiente().Extraer()
        while True:
            opcion = self.ValInt("Elija un categoria:", "Categoria no valida!")
            if opcion > 0 and opcion <= len(categoria):
                return categoria[opcion - 1]
            else:
                print("Categoria no valida!")

    def MenuEmpeado(self, opcion, Cola, Pila):
        print("\n====================================================================================")
        match opcion:
            case 1:
                atendido = Cola.pop()
                if atendido:
                    Pila.push(atendido)
                    print(f"Se ha atendido con éxito!")
                else:
                    print("No hay nadie en la cola para atender.")

            case 2:
                print("\n== Personas en espera ==")
                Cola.mostrar()

            case 3:
                print("\n== Historial ==")
                Pila.mostrar()

            case 4:
                dpi = input("Ingrese el DPI de la persona a eliminar de la cola: ")
                if Cola.eliminar(dpi):
                    print("Persona eliminada correctamente de la cola.")
                else:
                    print("No se encontró a nadie con ese DPI en la cola.")

            case 5:
                dpi = input("Ingrese el DPI de la persona a modificar en la cola: ")
                persona = Cola.buscar(dpi)
                if persona:
                    nombre = input("Ingrese el nuevo nombre: ")
                    persona.Nombre = nombre
                    print("Datos actualizados correctame")
                else:
                    print("Persona no encontrada en la fila")

            case 6:
                print(f"Cantidad en espera: {Cola.cantidad()}")

            case 7:
                print(f"Cantidad en historial: {Pila.cantidad()}")
            case 8:
                dpi = input("Ingrese el DPI a buscar en el historial: ")
                persona = Pila.buscar(dpi)
                if persona:
                    print("\nPersona encontrada")
                    persona.Mostrar()
                else:
                    print("No se encontró esa persona en el historial.")
            case _:
                print("Opcion no valida!")
