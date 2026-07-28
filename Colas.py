from collections import deque

class Cola:
    def __init__(self):
        self.__Cola = deque()

    def Push(self, agregar):
        self.__Cola.append(agregar)

    def Mostrar(self):
        for n, c in enumerate(self.__Cola, start=1):
            c.Mostrar()

    def EliminarPaciente(self, dpi):
        for p in self.__Cola:
            if p.Dpi == dpi:
                self.__Cola.remove(p)
                return True
        return False

    def PopCola(self):
        return self.__cola.popleft()

    def CantidadPila(self):
        return len(self.__pila)

