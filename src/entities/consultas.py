from entities.Videojuego import Videojuego
from utils.menus.Menus import menu_realizar_consultas
from utils.menus.MenuUtils import pedir_dato, limpiar_consola

""" 10 mejores desarrolladores registrados """
def top_10_devs(desarrolladores: list) -> dict:
    desarrolladores.sort(key=lambda dev: dev.experiencia, reverse=True)
    top_10_devs_por_exp = {}
    for index, dev in enumerate(desarrolladores[0:10]):
        top_10_devs_por_exp[index +
                            1] = f"{dev.ci} - {dev.nombre} - Experiencia: {dev.experiencia}"
    
    return top_10_devs_por_exp

"""  5 mejores desarrolladores con el rol de Programador """
def top_5_por_rol(desarrolladores: list) -> dict:
    programadores = desarrolladores.copy()

    # Obtengo todos los devs con rol "Programador"
    programadores = list(filter(lambda dev: dev.rol == "Programador", programadores))

    # Ordeno la lista de desarrolladores por su experiencia
    programadores.sort(key=lambda dev: dev.experiencia, reverse=True)

    top_5_programadores = {}
    
    for index, dev in enumerate(programadores[0:5]):
        top_5_programadores[index +
                            1] = f"{dev.ci} - {dev.nombre} - Experiencia: {dev.experiencia}"
        
    return top_5_programadores

""" 7 desarrolladores registrados con edad más avanzada """
def top_7_por_edad(desarrolladores: list) -> dict:
    devs_con_mas_edad = desarrolladores.copy()
    # Ordeno la lista de desarrolladores por su edad
    devs_con_mas_edad.sort(key=lambda dev: dev.edad, reverse=True)
    top_7_con_mas_edad = {}
    
    for index, dev in enumerate(devs_con_mas_edad[0:7]):
        top_7_con_mas_edad[index +
                            1] = f"{dev.ci} - {dev.nombre} - Edad: {dev.edad}"
    
    return top_7_con_mas_edad

""" videojuego con más desarrolladores que provienen de Uruguay """
def videojuego_por_cant_uruguayos(videojuegos: list) -> Videojuego:
    videojuegos = videojuegos.copy()
    
    videojuegos_cant_uruguayos = []
    
    for juego in videojuegos:
        
        devs_uruguayos = filter(lambda dev: dev.pais_origen == "Uruguay", juego.desarrolladores)
        cant_uruguayos = len(list(devs_uruguayos))
        info_juego = {
            "juego": juego.nombre,
            "cant_uruguayos": cant_uruguayos
        }
        videojuegos_cant_uruguayos.append(info_juego)
    videojuegos_cant_uruguayos.sort(key=lambda juego: juego["cant_uruguayos"], reverse=True)
    
    return videojuegos_cant_uruguayos[0]

def menu_consultas(desarrolladores: list, videojuegos: list):
        menu = menu_realizar_consultas
        opcion = None
        while opcion != "5":
            print(menu)
            opcion = input("Opción: ")
            limpiar_consola()
            match opcion:
                case "1":
                    resultado = top_10_devs(desarrolladores)
                    print("  Top 10 desarrolladores con mas experiencia\n")
                    print(resultado)
                case "2": 
                    resultado = top_5_por_rol(desarrolladores)
                    print("  Top 5 programadores con mas experiencia\n")
                    print(resultado)
                case "3": 
                    print("  Top 7 desarrolladores con edad mas avanzada\n")
                    resultado = top_7_por_edad(desarrolladores)
                    print(resultado)
                case "4": 
                    print("  Videojuego con más desarrolladores que provienen de Uruguay\n")
                    resultado = videojuego_por_cant_uruguayos(videojuegos)
                    print(resultado)
                case "5": return
                

        
        """ Categorias """
        """ print(menu)
        string_categorias = "Ingrese opcion \n  "
        string_categorias += "\n  ".join(
            [f"{categoria[0]} - {categoria[1]}" for categoria in self.posibles_categorias])
        string_categorias += "\n\n  Opción:"
        pedir_dato(self.validar_y_guardar_categorias, string_categorias)
        menu = f"{menu}\n|  Categoría/s: {self.categorias}"

        print("\n\n  Videojuego dado de alta con éxito!") """