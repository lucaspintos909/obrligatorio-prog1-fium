from utils.menus import limpiar_consola
from utils.menus import menu_principal

# Clases
from entities import Desarrollador

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
            case "2":
                print("Alta de videojuego")
            case "3":
                print("Simular competencia")
            case "4":
                print("Realizar consultas")
            case "5":
                input("Presione la tecla enter para salir...")
                print("Chau!")
                exit()
            case cualquier_otro:
                print("Opción inválida, intente nuevamente.")


limpiar_consola()
menu()
