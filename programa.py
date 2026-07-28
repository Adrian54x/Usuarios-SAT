from Validaciones import Validacion
from Persona import Persona
from Menus import Menus
import time

menu = Menus()
validacion = Validacion()

while True:
    try:
        print("\n====================================================================================")
        menu.principal()
        opcion = validacion.ValInt("Elija una opcion:", "Opcion invalida!")
        match opcion:
            case 0:
                print("\n====================================================================================")
                print("Saliendo", end="")
                time.sleep(0.5)
                print(".", end="")
                time.sleep(0.5)
                print(".", end="")
                time.sleep(0.5)
                print(".", end="")
                break

            case 1:
                while True:
                    print("\n====================================================================================")
                    menu.recepcion()
                    subOpcion = validacion.ValInt("Elija una opcion:", "Opcion invalida!")
                    if subOpcion == 0:
                        break
                    if(subOpcion not in [1,2,3,4,5]):
                        print("Opcion invalida")
                    else:
                        print("=== Usuario ===")
                        dpi = validacion.Dpi()
                        nombres = validacion.Nombre()
                        apellidos = validacion.Apellido()
                        fechaDeNacimiento = validacion.FechaNacimiento()
                        genero = validacion.Genero()
                        valExtranjero = validacion.SiNo("Es extranjero(SI / NO):")
                        valIdiomas = validacion.SiNo("Habla otro idioma(SI /NO):")

                        match subOpcion:
                            case 1:
                                persona = Persona(dpi, nombres, apellidos, fechaDeNacimiento,
                                                  genero,)
                            case _:
                                print("Opcion no existente!")

            case _:
                print("\n====================================================================================")
                print("Opcion no existente")
    except:
        print("Ha ocurrido un error")