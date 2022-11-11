
class Competencia:

    def __init__(self) -> None:
        self._videojuegos: list = []
        self._desarrolladores: list = []

    @property
    def videojuegos(self):
        return self._videojuegos
    
    @videojuegos.setter
    def videojuegos(self, videojuegos):
        self._videojuegos = videojuegos
    
    @property
    def desarrolladores(self):
        return self._desarrolladores
    
    @desarrolladores.setter
    def desarrolladores(self, desarrolladores):
        self._desarrolladores = desarrolladores