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
                """ def por_exp(dev):
                    return dev.experiencia
                devs.sort(key=por_exp, reverse=True)
                dict_perro= {}
                for index, dev  in enumerate(devs[0:10]):
                    dict_perro[index + 1] = f"{dev.ci} - {dev.nombre} - Experiencia: {dev.experiencia}" """

                def verificar_por_rol(dev):
                    return dev.rol == "Programador"

                devs = list(filter(verificar_por_rol, devs))

                def por_exp(dev):
                    return dev.experiencia

                devs.sort(key=por_exp, reverse=True)

                dict_gato = {}

                for index, dev in enumerate(devs[0:5]):
                    dict_gato[index +
                              1] = f"{dev.ci} - {dev.nombre} - Experiencia: {dev.experiencia}"

                print(dict_gato)
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
