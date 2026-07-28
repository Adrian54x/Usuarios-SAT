import idiomas
from Validaciones import Validacion
from Persona import Persona
from Menus import Menus
from Colas import Cola
from extranjero import Extranjero
from vehiculo import Vehiculos
import time

menu = Menus()
validacion = Validacion()
colaOP1 = Cola()
colaOP2 = Cola()
colaOP3 = Cola()
colaOP4 = Cola()
colaOP5 = Cola()
colaEspecial = Cola()

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
                        print("\n====================================================================================")
                        extranjero = False
                        print("=== Usuario ===")
                        dpi = validacion.Dpi()
                        nombres = validacion.Nombre()
                        apellidos = validacion.Apellido()
                        fechaDeNacimiento = validacion.FechaNacimiento()
                        genero = validacion.Genero()
                        if validacion.SiNo("Es extranjero(SI / NO):"):
                            extranjero = True
                            idiomas = validacion.Idioma()
                            pais = validacion.Pais()
                            contiente = validacion.Continente()


                        match subOpcion:
                            case 1:
                                print("Categorias:")
                                categoria = validacion.Categoria()
                                print("Tipo:")
                                tipo = validacion.Tipos(subOpcion)
                                prioridad = validacion.SiNo("Es prioridad(SI / NO):")
                                if prioridad:
                                    prioridad = "si"
                                else:
                                    prioridad = "no"
                                persona = Persona(dpi, nombres, apellidos, fechaDeNacimiento, genero, categoria, tipo, prioridad)
                                if prioridad == "no" and not extranjero:
                                    colaOP1.Push(persona)
                                else:
                                    if extranjero:
                                        persona = Extranjero(dpi, nombres, apellidos, fechaDeNacimiento, genero, categoria, tipo, idiomas, pais, contiente)
                                    colaEspecial.Push(persona)
                                print("\nUsuario Agregado a la cola!")

                            case 2:
                                print("Categorias:")
                                categoria = validacion.Categoria()
                                print("Tipo:")
                                tipo = validacion.Tipos(subOpcion)
                                print("Categoria de vehiculo:")
                                categoriaVehiculo = validacion.CategoriaVehiculo()
                                print("Tipo de vehiculo:")
                                tipoVehiculo = validacion.TipoVehiculo()
                                persona = Vehiculos(dpi, nombres, apellidos, fechaDeNacimiento, genero, categoria, tipo, categoriaVehiculo, tipoVehiculo)
                                if validacion.SiNo("Es prioridad(SI / NO):") or extranjero:
                                    if extranjero:
                                        persona = Extranjero(dpi, nombres, apellidos, fechaDeNacimiento, genero, categoria, tipo, idiomas, pais, contiente)
                                    colaEspecial.Push(persona)
                                else:
                                    colaOP2.Push(persona)

                            case 3:
                                print("Categorias:")
                                categoria = validacion.CategoriaOP3()
                                print("Tipo:")
                                tipo = validacion.Tipos(subOpcion)
                                prioridad = validacion.SiNo("Es prioridad(SI / NO):")
                                if prioridad:
                                    prioridad = "si"
                                else:
                                    prioridad = "no"
                                persona = Persona(dpi, nombres, apellidos, fechaDeNacimiento, genero, categoria, tipo, prioridad)
                                if prioridad == "si" or extranjero:
                                    if extranjero:
                                        persona = Extranjero(dpi, nombres, apellidos, fechaDeNacimiento, genero, categoria, tipo, idiomas, pais, contiente)
                                    colaEspecial.Push(persona)
                                else:
                                    colaOP3.Push(persona)

                            case 4:
                                print("Categorias:")
                                categoria = validacion.CategoriaOP4()
                                print("Tipo:")
                                tipo = validacion.Tipos(subOpcion)
                                if prioridad:
                                    prioridad = "si"
                                else:
                                    prioridad = "no"
                                persona = Persona(dpi, nombres, apellidos, fechaDeNacimiento, genero,  categoria, tipo, prioridad)
                                if prioridad == "si" or extranjero:
                                    if extranjero:
                                        persona = Extranjero(dpi, nombres, apellidos, fechaDeNacimiento, genero, categoria, tipo, idiomas, pais, contiente)
                                    colaEspecial.Push(persona)
                                else:
                                    colaOP4.Push(persona)

                            case 5:
                                print("Categorias:")
                                categoria = validacion.CategoriaOP5()
                                print("Tipo:")
                                tipo = validacion.Tipos(subOpcion)
                                if prioridad:
                                    prioridad = "si"
                                else:
                                    prioridad = "no"
                                persona = Persona(dpi, nombres, apellidos, fechaDeNacimiento, genero, categoria, tipo, prioridad)
                                if prioridad == "si" or extranjero:
                                    if extranjero:
                                        persona = Extranjero(dpi, nombres, apellidos, fechaDeNacimiento, genero, categoria, tipo, idiomas, pais, contiente)
                                    colaEspecial.Push(persona)
                                else:
                                    colaOP5.Push(persona)
            case 2:
                print("\n====================================================================================")
                menu.recepcion()
            case _:
                print("\n====================================================================================")
                print("Opcion no existente")
    except:
        print("Ha ocurrido un error")