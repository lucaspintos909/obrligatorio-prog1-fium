opciones_menu="""
------------------
| Menú Principal |
------------------
Seleccione alguna opción del manú:
    1. Alta de desarrollador
    2. Alta de videojuego
    3. Simular competencia
    4. Realizar consultas
    5. Finalizar programa

"""
def menu():
    option = None
    while option != "5":
        print(opciones_menu)
        option = input("Opción: ")
        match(option):
            case "1":
                print("Alta de desarrollador")
            case "2":
                print("Alta de videojuego")
            case "3":
                print("Simular competencia")
            case "4":
                print("Realizar consultas")
            case "5":
                print("Chau!")
            case other:
                print("Opción inválida, intente nuevamente.")

menu()