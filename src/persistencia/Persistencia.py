import csv
from entities.Desarrollador import Desarrollador

ruta_archivo_desarrolladores = "./src/persistencia/desarrolladores.csv"

def guardar_desarrolladores(desarrolladores: list):
    desarrollador_header = ["ci", "nombre", "apellido",
                            "pais_origen", "fecha_nacimiento", "experiencia", "rol", "asignado"]
    
    desarrolladores_data =  list(map(lambda dev: dev.obtener_dict(), desarrolladores))

    with open(ruta_archivo_desarrolladores, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=desarrollador_header)
        writer.writeheader()
        writer.writerows(desarrolladores_data)

def cargar_desarrolladores() -> list:
    desarrolladores = []
    with open(ruta_archivo_desarrolladores, 'r') as file:
        csvreader = csv.DictReader(file)
        for dev in csvreader:
            if "ci" in dev:
                desarrollador = Desarrollador()
                desarrollador.cargar_desde_dict(dev)
                desarrolladores.append(desarrollador)
    return desarrolladores