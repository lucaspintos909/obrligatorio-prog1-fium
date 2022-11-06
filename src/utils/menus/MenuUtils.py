from os import name, system

def limpiar_consola():
    # Para windows
    if name == 'nt':
        system('cls')
    # Para mac y linux
    else:
        system('clear')

def pedir_dato(setter, string_input: str):
    dato_ok = False
    while not dato_ok:
        dato_ingresado = input(f"|  {string_input}")
        try:
            setter(dato_ingresado)
            dato_ok = True
            
        except Exception as error:
            print(f"|  ***** ")
            print(f"|  ERROR: {error}, intente nuevamente.")
            print(f"|  ***** ")
            print(f"|  ")
