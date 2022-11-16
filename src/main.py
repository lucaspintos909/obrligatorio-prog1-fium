from utils.menus.MenuUtils import limpiar_consola
from utils.menus.Menus import menu_principal

# Clases
from entities.Desarrollador import Desarrollador
from entities.Videojuego import Videojuego
from entities.Competencia import Competencia

from persistencia.Persistencia import guardar_desarrolladores, cargar_desarrolladores, guardar_videojuegos, cargar_videojuegos

from entities.consultas import menu_consultas

competencia = Competencia()
competencia.desarrolladores = cargar_desarrolladores()
competencia.videojuegos = cargar_videojuegos(competencia.desarrolladores)


def main():
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
                desarrolladores = competencia.desarrolladores.copy()
                videojuegos = competencia.videojuegos.copy()
                menu_consultas(desarrolladores, videojuegos)
                
            case "5":
                raise KeyboardInterrupt()
            case cualquier_otro:
                print("Opción inválida, intente nuevamente.")


limpiar_consola()
try:
    main()
except KeyboardInterrupt:
    guardar_desarrolladores(competencia.desarrolladores)
    guardar_videojuegos(competencia.videojuegos)
    print("\n\nChau!")

    exit()
