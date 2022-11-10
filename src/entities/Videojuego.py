
from utils.menus.MenuUtils import pedir_dato
from utils.menus.Menus import menu_alta_videojuego
from exceptions.DatosInvalidos import DatosInvalidos


class Videojuego:
    posibles_categorias = [(1, "Acción"), (2, "Aventura"), (3, "Estrategia"), (4, "Puzzle")]

    def __init__(self):
        self._nombre: str = None
        self._categorias: list = None
        self._desarrolladores: list = None

    @property
    def nombre(self):
        return self._nombre

    def validar_y_guardar_nombre(self, nombre: str):
        mensaje_error = "El nombre ingresado es inválido, debe tener entre 2 y 100 carácteres"
        if type(nombre) is not str or len(nombre) < 2 or len(nombre) > 100:
            raise DatosInvalidos(mensaje_error)
        self._nombre = nombre

    @property
    def categorias(self):
        return ", ".join(map(lambda id: self.obtener_categoria_por_id(id)[1], self._categorias))
    
    def validar_y_guardar_categorias(self, categorias_ingresadas: str):
        mensaje_error = "La/s categorías ingresadas son inválidas, ingrese al menos un número de la lista, o varios de la siguiente manera: 1,2,3,...etc"
        # Genero una lista de numeros
        # Las categorias ingresadas vienen de la forma "1,2,3,4"
        # Con el split(",") separa el string por comas y genera una lista de la forma ["1","2","3","4"]
        categorias = categorias_ingresadas.split(",")
        es_valido = True
        
        # Me fijo si el usuario ingresó una cantidad mayor a la cantidad de categorias o si no ingresó nada directamente
        if len(categorias) > len(self.posibles_categorias) or len(categorias) == 0:
            es_valido = False
            
        for categoria in categorias:
            # Me fijo si la categoria es un numero, y si existe esa categoria
            if not categoria.isnumeric() or not self.obtener_categoria_por_id(int(categoria)):
                es_valido = False
                break

        if not es_valido:
            raise DatosInvalidos(mensaje_error)
        
        # Convierto la lista de strings a numeros (Ej: ["1", "2"] a [1, 2]) y lo guardo en las categorias de la clase. 
        self._categorias = list(map(lambda id: int(id), categorias))
    
    def obtener_categoria_por_id(self, id: int) -> bool | object:
        categoria = False
        for id_categoria, nombre_categoria in self.posibles_categorias:
            if id_categoria == id:
                categoria = (id_categoria, nombre_categoria)
                break
        return categoria

    @property
    def desarrolladores(self):
        return self._desarrolladores

    def menu_de_alta(self):
        menu = menu_alta_videojuego

        """ Nombre """
        print(menu)
        string_nombre = "Ingrese nombre del videojuego:"
        pedir_dato(self.validar_y_guardar_nombre, string_nombre)
        menu = f"{menu}\n|  Nombre: {self.nombre}"
        
        """ Categorias """
        print(menu)
        string_categorias = "Ingrese categoría/s del videojuego (si es mas de una, se separa por comas, ej: 1,2,3,4) \n  "
        string_categorias += "\n  ".join([f"{categoria[0]} - {categoria[1]}" for categoria in self.posibles_categorias])
        string_categorias += "\n\n  Opción:"
        pedir_dato(self.validar_y_guardar_categorias, string_categorias)
        menu = f"{menu}\n|  Categoría/s: {self.categorias}"
        
        print(menu)
