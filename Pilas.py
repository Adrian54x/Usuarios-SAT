class Pilas:
    def __init__(self):
        self.__pila = []

    def push(self, cliente):
        self.__pila.append(cliente)

    def mostrar(self):
        if not self.__pila:
            print("El historial está vacío.")
            return
        for n, c in enumerate(reversed(self.__pila), start=1):
            print(f"{n}.")
            c.Mostrar()

    def cantidad(self):
        return len(self.__pila)

    def buscar_persona(self, dpi):
        for p in self.__pila:
            if int(p.Dpi) == int(dpi):
                return p
        return None