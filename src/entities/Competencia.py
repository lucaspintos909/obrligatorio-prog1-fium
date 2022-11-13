from utils.menus.MenuUtils import pedir_dato
from utils.menus.Menus import menu_simular_competencia
from exceptions.DatosInvalidos import DatosInvalidos
from entities.Videojuego import Videojuego
from entities.Desarrollador import Desarrollador


class Competencia:

    def __init__(self) -> None:
        self._videojuegos: list = []
        self._desarrolladores: list = []
        self._resultado_ultima_competencia: dict = {}

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

    @property
    def resultado_ultima_competencia(self):
        return self._resultado_ultima_competencia

    @resultado_ultima_competencia.setter
    def resultado_ultima_competencia(self, resultado):
        self._resultado_ultima_competencia = resultado

    def validar_datos_y_simular(self, categoria_ingresada: str):
        mensaje_error = "La categoría ingresada es inválida, ingrese un número de la lista"
        if not categoria_ingresada.isnumeric():
            raise DatosInvalidos(mensaje_error)

        # Busco la categoria por el id que ingresó el usuario
        categoria = None
        for categ in Videojuego.posibles_categorias:
            if categ[0] == int(categoria_ingresada):
                # Me guardo la cateoria
                categoria = categ
                break

        # Chequeo si encontro la categoría
        if len(categoria) == 0:
            raise DatosInvalidos(mensaje_error)

        # Obtengo todos los videojuegos con la categoria indicada
        videojuegos = list(
            filter(lambda juego: categoria[1] in juego.categorias, self.videojuegos))

        podio_juegos = []
        """
            De la forma:
            [{ 
              "nombre": NombreRandom, 
              "promedios_por_rol": {"rol1": 3.5, "rol2": 5.1}, 
              "cant_desarrolladores": 9,
              "promedio": 4
            },
            { 
              "nombre": NombreRandom2, 
              "promedios_por_rol": {"rol1": 3.5, "rol2": 5.1}, 
              "cant_desarrolladores": 5,
              "promedio": 8
            }]
        """

        for juego in videojuegos:
            promedios_juego = {
                "nombre": juego.nombre,
                "promedios_por_rol": {},
                "cant_desarrolladores": len(juego.desarrolladores)
            }

            for _, rol in Desarrollador.roles_permitidos:
                promedios_juego["promedios_por_rol"][rol] = juego.obtener_promedio_experiencia_por_rol(
                    rol)
            podio_juegos.append(promedios_juego)

        # Hago los calculos en cada juego y lo guardo en promedio
        for juego in podio_juegos:
            promedios_por_rol = juego["promedios_por_rol"]
            promedio_juego = 0.2 * promedios_por_rol["Diseñador"]
            promedio_juego += 0.12 * promedios_por_rol["Productor"]
            promedio_juego += 0.5 * promedios_por_rol["Programador"]
            promedio_juego += 0.18 * promedios_por_rol["Tester"]

            juego["promedio"] = promedio_juego

        # Ordeno por promedio y en orden de mayor a menor
        podio_juegos.sort(key=lambda dev: dev["promedio"], reverse=True)

        for index in range(len(podio_juegos) - 1):
            juego = podio_juegos[index]
            juego_siguiente = podio_juegos[index + 1]
            # Si algún promedio del podio da igual
            if juego["promedio"] == juego_siguiente["promedio"]:
                nuevo_orden = [juego, juego_siguiente]
                if juego["cant_desarrolladores"] != juego_siguiente["cant_desarrolladores"]:
                    # Si la cantidad de desarrolladores no es la misma ordeno por cantidad
                    nuevo_orden.sort(
                        key=lambda item: item["cant_desarrolladores"], reverse=True)
                else:
                    # Si la cantidad de desarrolladores es la misma ordeno por nombre
                    nuevo_orden.sort(
                        key=lambda item: item["nombre"], reverse=True)

                # Cambio el orden del podio por el nuevo orden
                podio_juegos[index] = nuevo_orden[0]
                podio_juegos[index + 1] = nuevo_orden[1]

        # Guardo el resultado
        self.resultado_ultima_competencia = {
            "categoria": categoria,
            "podio": podio_juegos
        }

        return ""

    def menu_simulacion(self):
        menu = menu_simular_competencia
        """ Categoría """
        print(menu)
        string_categorias = "Ingrese la categoría del videojuego \n  "
        string_categorias += "\n  ".join(
            [f"{categoria[0]} - {categoria[1]}" for categoria in Videojuego.posibles_categorias])
        string_categorias += "\n\n  Opción:"
        pedir_dato(self.validar_datos_y_simular, string_categorias)
        
        """ Resultado """
        categoria = self.resultado_ultima_competencia['categoria']
        podio = self.resultado_ultima_competencia['podio']
        
        menu = f"{menu}\n|  Categoría: {categoria[1]}\n"
        if len(podio) == 0:
            menu = f"{menu}\n   No hay videojuegos para esta categoría"
            print(menu)
            return
        if len(podio) >= 1:
            menu = f"{menu}\n   1er puesto: {podio[0]['nombre']}"
            menu = f"{menu}\n       Promedio: {podio[0]['promedio']}\n"
        if len(podio) >= 2:
            menu = f"{menu}\n   2do puesto: {podio[1]['nombre']}"
            menu = f"{menu}\n       Promedio: {podio[1]['promedio']}\n"
        if len(podio) >= 3:
            menu = f"{menu}\n   3er puesto: {podio[2]['nombre']}"
            menu = f"{menu}\n       Promedio: {podio[2]['promedio']}\n"

        print(menu)
