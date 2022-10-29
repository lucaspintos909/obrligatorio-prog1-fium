
class Competencia:

    def __init__(self, categoria: str) -> None:
        self.juegos: list = []
        self.categoria: str = categoria
        self.podio: list = []
