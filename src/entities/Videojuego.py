
class Videojuego:
    posibles_categorias = ["Acción", "Aventura", "Estrategia", "Puzzle"]

    def __init__(self, nombre: str, categorias: list, desarrolladores: list):
        self._nombre = nombre
        self._categorias = categorias
        self._desarrolladores = desarrolladores
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def categorias(self):
        return self._categorias

    @property
    def desarrolladores(self):
        return self._desarrolladores