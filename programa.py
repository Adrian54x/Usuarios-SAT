import Validaciones

validacion = Validaciones.Validacion()

while True:
    try:
        opcion = validacion.ValInt("Elija una opcion:", "Opcion invalida!")
        match opcion:
            case 1:
                subOpcion = validacion.ValInt("Elija una opcion:", "Opcion invalida!")
                if(subOpcion not in [1,2,3,4,5]):
                    print("Opcion invalida")
                else:
                    print("=== Usuario ===")
                    dpi = validacion.Dpi()
                    nombres = validacion.Nombre()
                    apellidos = validacion.Apellido()
                    fechaDeNacimiento = validacion.FechaNacimiento()
                    genero = validacion.Genero()
                    match subOpcion:
                        case _:
                            print("Opcion no existente!")
            case _:
                print("Opcion no existente")
    except:
        print("Ha ocurrido un error")