
class Competencia:

    def __init__(self, categoria: str) -> None:
        self._videojuegos: list = []
        self._categoria: str = categoria
        self._podio: list = []
        