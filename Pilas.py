class Pilas:
    def __init__(self, pila : list):
        self.__Pila = pila

    def Push(self, agregar):
        self.__Pila.append(agregar)

    def Mostrar(self):
        for n, c in enumerate(self.__Pila, start=1):
            c.Mostrar()