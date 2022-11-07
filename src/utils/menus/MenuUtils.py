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
        # Pido el dato
        dato_ingresado = input(f"\n  {string_input} ")
        try:
            # Uso el setter, y si se guarda correctamente borro los errores
            setter(dato_ingresado)
            dato_ok = True
            limpiar_consola()

        except Exception as error:
            print(f"\n  ***** ")
            print(f"  ERROR: {error}, intente nuevamente.")
            print(f"  ***** ")
