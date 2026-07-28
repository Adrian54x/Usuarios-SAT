from collections import deque

class Cola:
    def __init__(self):
        self.__cola = deque()

    def Push(self, agregar):
        self.__cola.append(agregar)

    def pop(self):
        if len(self.__cola) > 0:
            return self.__cola.popleft()
        return None

    def eliminar(self, dpi):
        for p in self.__cola:
            if int(p.Dpi) == int(dpi):
                self.__cola.remove(p)
                return True
        return False

    def mostrar(self):
        if not self.__cola:
            print("La cola está vacía.")
            return
        for n, c in enumerate(self.__cola, start=1):
            print(f"--- Posición {n} ---")
            c.Mostrar()

    def buscar(self, dpi):
        for p in self.__cola:
            if int(p.Dpi) == int(dpi):
                return p
        return None

    def cantidad(self):
        return len(self.__cola)
