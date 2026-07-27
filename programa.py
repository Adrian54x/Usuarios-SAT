import Usuario
import Validaciones

usuario = Usuario.Usuarios()
validacion = Validaciones.Validacion()

while True:
    try:
        opcion = validacion.ValInt("Elija una opcion", "Opcion invalida!")
        match opcion:
            case 1:
                print("Ha ocurrido un error")
            case _:
                print("Opcion no existente")
    except:
        print("Ha ocurrido un error")