from utils.menus.MenuUtils import limpiar_consola
from utils.menus.Menus import menu_principal

# Clases
from entities.Desarrollador import Desarrollador
from entities.Videojuego import Videojuego
from entities.Competencia import Competencia

from persistencia.Persistencia import guardar_desarrolladores, cargar_desarrolladores, guardar_videojuegos, cargar_videojuegos

competencia = Competencia()
competencia.desarrolladores = cargar_desarrolladores()
competencia.videojuegos = cargar_videojuegos(competencia.desarrolladores)


def menu():
    opcion = None
    while opcion != "5":
        print(menu_principal)
        opcion = input("Opción: ")
        limpiar_consola()
        match opcion:
            case "1":
                desarrollador = Desarrollador()
                desarrollador.menu_de_alta()
                competencia.desarrolladores += [desarrollador]

                guardar_desarrolladores(competencia.desarrolladores)

            case "2":
                videojuego = Videojuego()
                videojuego.menu_de_alta(competencia.desarrolladores)
                competencia.videojuegos += [videojuego]

            case "3":
                competencia.menu_simulacion()

            case "4":
                devs = competencia.desarrolladores.copy()
                """ 10 mejores desarrolladores registrados """
                def por_exp(dev):
                    return dev.experiencia

                devs.sort(key=lambda dev: dev.experiencia, reverse=True)
                top_10_devs_por_exp = {}
                for index, dev in enumerate(devs[0:10]):
                    top_10_devs_por_exp[index +
                                        1] = f"{dev.ci} - {dev.nombre} - Experiencia: {dev.experiencia}"

                """  5 mejores desarrolladores con el rol de Programador """
                programadores = competencia.desarrolladores.copy()

                # Obtengo todos los devs con rol "Programador"
                programadores = list(filter(lambda dev: dev.rol == "Programador", devs))

                # Ordeno la lista de desarrolladores por su experiencia
                programadores.sort(key=lambda dev: dev.experiencia, reverse=True)

                top_5_programadores = {}
                
                for index, dev in enumerate(programadores[0:5]):
                    top_5_programadores[index +
                                        1] = f"{dev.ci} - {dev.nombre} - Experiencia: {dev.experiencia}"

                """ 7 desarrolladores registrados con edad más avanzada """
                devs_con_mas_edad = competencia.desarrolladores.copy()
                # Ordeno la lista de desarrolladores por su edad
                devs_con_mas_edad.sort(key=lambda dev: dev.edad, reverse=True)
                top_7_con_mas_edad = {}
                
                for index, dev in enumerate(devs_con_mas_edad[0:15]):
                    top_7_con_mas_edad[index +
                                        1] = f"{dev.ci} - {dev.nombre} - Edad: {dev.edad}"

                """ videojuego con más desarrolladores que provienen de Uruguay """
                videojuegos = competencia.videojuegos.copy()
                
                videojuegos_cant_uruguayos = []
                
                for juego in videojuegos:
                    
                    devs_uruguayos = filter(lambda dev: dev.pais_origen == "Uruguay", juego.desarrolladores)
                    cant_uruguayos = len(list(devs_uruguayos))
                    info_juego = {
                        "juego": juego,
                        "cant_uruguayos": cant_uruguayos
                    }
                    videojuegos_cant_uruguayos.append(info_juego)
                videojuegos_cant_uruguayos.sort(key=lambda juego: juego["cant_uruguayos"], reverse=True)

            case "5":
                raise KeyboardInterrupt()
            case cualquier_otro:
                print("Opción inválida, intente nuevamente.")


limpiar_consola()
try:
    menu()
except KeyboardInterrupt:
    guardar_desarrolladores(competencia.desarrolladores)
    guardar_videojuegos(competencia.videojuegos)
    print("\n\nChau!")

    exit()
