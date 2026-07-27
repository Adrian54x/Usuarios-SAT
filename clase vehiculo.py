class Vehiculos:
    def __init__(self,categoria,tipo):
        self.categoria = categoria
        self.tipo = tipo

    def mostrar_vehiculo(self):
        print("La informacion del vehiculo es la siguiente:_ ")
        print("")
        print("Categoria del vehiculo:_ ",self.categoria)
        print("")
        print("Tipo de vehiculo:_ ",self.tipo)

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self,categoria):
        if categoria not in ["Terrestre","Aereo","Acuatico"]:
            print("Error, no se ha ingresado una categoria valida")
        else:
            self.__categoria = categoria

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,tipo):
        if tipo not in ["Particular","Comercial","Alquiler","Urbano","Diplomatico","Oficial","Motocicleta"]:
            print("Error, no se ha ingresado un tipo valido de vehiculo")
        else:
            self.__tipo = tipo