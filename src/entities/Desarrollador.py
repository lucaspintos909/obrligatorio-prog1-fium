from utils.menus import limpiar_consola, menu_alta_desarrollador
from utils.menus import pedir_dato
from exceptions import DatosInvalidos

class Desarrollador:
    # Esto lo pongo acá para tener una guía
    paises_permitidos = ["Argentina", "Brasil", "Chile", "Uruguay"]
    roles_permitidos = ["diseñador", "productor", "programador", "tester"]

    def __init__(self):
        self._ci: int = None
        self._nombre: str = None
        self._apellido: str = None
        self._pais_origen: str = None
        self._fecha_nacimiento: str = None
        self._experiencia: int = None
        self._rol: str = None

    @property
    def ci(self):
        return self._ci

    def ci_setter(self, ci):
        mensaje_error = "La cedula ingresada es inválida, debe tener 8 digitos, incluyendo verificador y no debe tener puntos ni guiónes"
        if len(ci) != 8 or not ci.isnumeric():
            raise DatosInvalidos(mensaje_error)
        self._ci = int(ci)

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def pais_origen(self):
        return self._pais_origen

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @property
    def experiencia(self):
        return self._experiencia

    @property
    def rol(self):
        return self._rol

    def menu_de_alta(self):
        limpiar_consola()
        print(menu_alta_desarrollador)
        string = "Ingrese cédula: "
        pedir_dato(self.ci_setter, "Ingrese cédula (sin puntos ni guiónes): ")
