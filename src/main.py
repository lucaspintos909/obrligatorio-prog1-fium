import utils.MenuUtils as MenuUtils

opciones_menu = """
------------------------------
| Menú principal         - x |
------------------------------
|  1. Alta de desarrollador  |
|  2. Alta de videojuego     |
|  3. Simular competencia    |
|  4. Realizar consultas     |
|  5. Salir                  |
------------------------------
"""
def menu():
    opcion = None
    while opcion != "5":
        print(opciones_menu)
        opcion = input("Opción: ")
        MenuUtils.limpiar_consola()
        match opcion:
            case "1":
                print("Alta de desarrollador")
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


MenuUtils.limpiar_consola()
menu()
