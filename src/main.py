from utils.menus.MenuUtils import limpiar_consola
from utils.menus.Menus import menu_principal

# Clases
from entities.Desarrollador import Desarrollador
from entities.Videojuego import Videojuego

# Datos de ejemplos 
from datos_ejemplo import desarrolladores_prueba

desarrolladores = desarrolladores_prueba

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
                desarrolladores.append(desarrollador)
            case "2":
                videojuego = Videojuego()
                videojuego.menu_de_alta(desarrolladores)
            case "3":
                print("Simular competencia")
            case "4":
                print("Realizar consultas")
            case "5":
                input("Presione enter para salir...")
                print("Chau!")
                exit()
            case cualquier_otro:
                print("Opción inválida, intente nuevamente.")


limpiar_consola()
try:
    menu()
except KeyboardInterrupt:
    print("\n\nChau!")
    exit()
