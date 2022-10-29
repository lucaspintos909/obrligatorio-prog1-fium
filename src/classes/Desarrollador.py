
class Desarrollador:
    paises_permitidos = ["Argentina", "Brasil", "Chile", "Uruguay"]
    roles_permitidos = ["Diseñador", "Productor", "Programador", "Tester"]

    def __init__(self, ci: int, nombre: str, apellido: str, pais_origen: str, fecha_nacimiento: str, experiencia: int, rol: str ) -> None:
        self._ci = ci
        self._nombre = nombre
        self._apellido = apellido
        self._pais_origen = pais_origen
        self._fecha_nacimiento = fecha_nacimiento
        self._experiencia = experiencia
        self._rol = rol

    @property
    def ci(self):
        return self._ci

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