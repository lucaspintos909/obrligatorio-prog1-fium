
from utils.menus.MenuUtils import pedir_dato
from utils.menus.Menus import menu_alta_videojuego
from exceptions.DatosInvalidos import DatosInvalidos


class Videojuego:
    posibles_categorias = [(1, "Acción"), (2, "Aventura"),
                           (3, "Estrategia"), (4, "Puzzle")]

    def __init__(self):
        self._nombre: str = None
        self._categorias: list = []
        self._desarrolladores: list = []

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

    def validar_y_guardar_desarrollador(self, cedula_desarrollador_ingresado: str, desarrolladores: list) -> bool:
        mensaje_error = "La cedula del desarrollador ingresada es inválida, debe tener 8 digitos, incluyendo verificador y no debe tener puntos ni guiónes"
        if cedula_desarrollador_ingresado == "0":
            if self.verificar_composicion():
                return -1
            else:
                raise DatosInvalidos("La composicion del equipo no está completa, debe ingresar como mínimo 2 diseñadores, 1 productor, 3 programadores y 2 tester")
                
        if len(cedula_desarrollador_ingresado) != 8 or not cedula_desarrollador_ingresado.isnumeric():
            raise DatosInvalidos(mensaje_error)

        dev_encontrado = False
        # Busco el desarrollador en la lista general de desarrolladores
        for dev in desarrolladores:
            # Hago match por CI
            if dev.ci == int(cedula_desarrollador_ingresado):
                # Verifico si ya está asignado a algún videojuego
                if dev.asignado:
                    raise DatosInvalidos(
                        "El desarrollador ingresado ya pertenece a un videojuego")
                dev_encontrado = dev
                break

        # Si no encuentra al desarrollador lanza excepcion
        if not dev_encontrado:
            raise DatosInvalidos("El desarrollador ingresado no existe")

        # Si lo encontró entonces lo asigna al videojuego
        dev_encontrado.asignado = True
        self._desarrolladores.append(dev_encontrado)

    def verificar_composicion(self) -> bool:
        contador_devs_rol = {
            "Diseñador": 0,
            "Productor": 0,
            "Programador": 0,
            "Tester": 0
        }

        for desarrollador in self._desarrolladores:
            # Aumento el contador en el rol del dev
            contador_devs_rol[desarrollador.rol] += 1

        roles_ok = True

        if contador_devs_rol["Diseñador"] < 2 or contador_devs_rol["Productor"] < 1 or contador_devs_rol["Programador"] < 3 or contador_devs_rol["Tester"] < 2:
            roles_ok = False

        return roles_ok

    def obtener_dict(self):
        # Creo una lista de ci de los desarrolladores 
        lista_ci_devs = list(map(lambda dev: str(dev.ci), self._desarrolladores))
        lista_categorias = list(map(lambda cate: str(cate), self._categorias))
        return {
            "nombre": self._nombre,
            "categorias": "-".join(lista_categorias),
            "desarrolladores": "-".join(lista_ci_devs)
        }

    def cargar_desde_dict(self, videojuego: dict, desarrolladores: list):
        self._nombre = videojuego["nombre"]
        # Las categorias vienen de la forma "1-2-3", por eso le hago split por "-"
        self._categorias = list(map(lambda cate: int(cate), videojuego["categorias"].split("-")))
        # Los desarrolladores vienen de la forma "52650714-12345678-87654321", por eso le hago split por "-"
        ci_devs = videojuego["desarrolladores"].split("-")
        for ci in ci_devs:
            # Filtro los desarrolladores generales por ci y se lo agrego a desarrolladores
            self._desarrolladores += list(filter(lambda dev: dev.ci == int(ci), desarrolladores))

    def menu_de_alta(self, desarrolladores: list):
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

        """ Desarrolladores """
        print(menu)
        string_desarrollador = "Ingrese la cédula del desarrollador (ingrese 0 para dejar de agregar):"
        seguir_ingresando = None
        while seguir_ingresando != -1:
            seguir_ingresando = pedir_dato(self.validar_y_guardar_desarrollador,
                                           string_desarrollador, desarrolladores)
            print(f"{menu}\n|  Desarrolladores ingresados: ")
            for desarrollador in self.desarrolladores:
                print(f"|  {desarrollador}")

        print("\n\n  Videojuego dado de alta con éxito!")
