import csv
from entities.Desarrollador import Desarrollador
from entities.Videojuego import Videojuego

ruta_csv_desarrolladores = "./src/persistencia/desarrolladores.csv"
ruta_csv_videojuegos = "./src/persistencia/videojuegos.csv"

def guardar_desarrolladores(desarrolladores: list):
    desarrollador_header = ["ci", "nombre", "apellido",
                            "pais_origen", "fecha_nacimiento", "experiencia", "rol", "asignado"]
    
    desarrolladores_data =  list(map(lambda dev: dev.obtener_dict(), desarrolladores))

    with open(ruta_csv_desarrolladores, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=desarrollador_header)
        writer.writeheader()
        writer.writerows(desarrolladores_data)

def cargar_desarrolladores() -> list:
    desarrolladores = []
    with open(ruta_csv_desarrolladores, 'r') as file:
        csvreader = csv.DictReader(file)
        for dev in csvreader:
            if "ci" in dev:
                desarrollador = Desarrollador()
                desarrollador.cargar_desde_dict(dev)
                desarrolladores.append(desarrollador)
    return desarrolladores

def guardar_videojuegos(videojuegos: list):
    videojuego_header = ["nombre", "categorias", "desarrolladores"]
    
    videojuegos_data =  list(map(lambda dev: dev.obtener_dict(), videojuegos))

    with open(ruta_csv_videojuegos, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=videojuego_header)
        writer.writeheader()
        writer.writerows(videojuegos_data)

def cargar_videojuegos(desarrolladores: list) -> list:
    videojuegos = []
    with open(ruta_csv_videojuegos, 'r') as file:
        csvreader = csv.DictReader(file)
        for juego in csvreader:
            if "nombre" in juego:
                videojuego = Videojuego()
                videojuego.cargar_desde_dict(juego, desarrolladores)
                videojuegos.append(videojuego)
    return videojuegos