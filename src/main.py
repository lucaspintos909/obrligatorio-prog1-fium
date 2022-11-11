from utils.menus.MenuUtils import limpiar_consola
from utils.menus.Menus import menu_principal

# Clases
from entities.Desarrollador import Desarrollador
from entities.Videojuego import Videojuego
from entities.Competencia import Competencia

# Datos de ejemplos 
from datos_ejemplo import desarrolladores_prueba

competencia = Competencia()
competencia.desarrolladores = desarrolladores_prueba


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
                competencia.desarrolladores +=  [desarrollador]
            case "2":
                videojuego = Videojuego()
                videojuego.menu_de_alta(competencia.desarrolladores)
                competencia.videojuegos +=  [videojuego]
                
            case "3":
                print("Simular competencia")
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
                
                dict_gato= {}
                
                for index, dev  in enumerate(devs[0:5]):
                    dict_gato[index + 1] = f"{dev.ci} - {dev.nombre} - Experiencia: {dev.experiencia}"

                print(dict_gato)
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
