from os import name, system

def limpiar_consola():
    # Para windows
    if name == 'nt':
        system('cls')
    # Para mac y linux
    else:
        system('clear')