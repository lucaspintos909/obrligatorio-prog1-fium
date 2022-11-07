from datetime import date, timedelta
from utils.menus import limpiar_consola, menu_alta_desarrollador
from utils.menus import pedir_dato
from exceptions import DatosInvalidos


class Desarrollador:
    # Esto lo pongo acá para tener una guía
    paises_permitidos = [(1, "Argentina"), (2, "Brasil"),
                         (3, "Chile"), (4, "Uruguay")]
    roles_permitidos = [(1, "Diseñador"), (2, "Productor"), (3, "Programador"), (4, "Tester")]

    def __init__(self):
        self._ci: int = None
        self._nombre: str = None
        self._apellido: str = None
        self._pais_origen: str = None
        self._fecha_nacimiento: date = None
        self._edad: int = None
        self._experiencia: int = None
        self._rol: str = None

    @property
    def ci(self):
        return self._ci

    def validar_y_guardar_ci(self, ci: str):
        mensaje_error = "La cedula ingresada es inválida, debe tener 8 digitos, incluyendo verificador y no debe tener puntos ni guiónes"
        if len(ci) != 8 or not ci.isnumeric():
            raise DatosInvalidos(mensaje_error)
        self._ci = int(ci)

    @property
    def nombre(self):
        return self._nombre

    def validar_y_guardar_nombre(self, nombre: str):
        mensaje_error = "El nombre ingresado es inválido, debe tener entre 3 y 100 carácteres"
        if type(nombre) is not str or len(nombre) < 3 or len(nombre) > 100:
            raise DatosInvalidos(mensaje_error)
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    def validar_y_guardar_apellido(self, apellido: str):
        mensaje_error = "El apellido ingresado es inválido, debe tener entre 3 y 100 carácteres"
        if type(apellido) is not str or len(apellido) < 3 or len(apellido) > 100:
            raise DatosInvalidos(mensaje_error)
        self._apellido = apellido

    @property
    def pais_origen(self):
        pais = "Ninguno"
        for id_pais, nombre_pais in self.paises_permitidos:
            if id_pais == self._pais_origen:
                pais = nombre_pais
                break
        return pais

    def validar_y_guardar_pais_origen(self, pais_ingresado: str):
        mensaje_error = "El país ingresado es inválido, ingrese un número de la lista"
        if not pais_ingresado.isnumeric():
            raise DatosInvalidos(mensaje_error)

        # Busco si existe el pais ingresado
        pais = None
        for id_pais, nombre in self.paises_permitidos:
            if id_pais == int(pais_ingresado):
                pais = (id_pais, nombre)
                break
        if not pais:
            raise DatosInvalidos(mensaje_error)
        self._pais_origen = int(pais_ingresado)

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento.strftime("%d/%m/%Y")

    def validar_y_guardar_fecha_nacimiento(self, fecha_ingresada: str):
        mensaje_error = "La fecha ingresada es inválida, debe ingresar la fecha con el formato 'DD/MM/YYYY' y ser menor a la fecha de hoy"
        # Si el split no devuelve 3 elementos es porque esta mal el formato
        if len(fecha_ingresada.split('/')) != 3:
            raise DatosInvalidos(mensaje_error)

        dia, mes, año = fecha_ingresada.split('/')
        fecha_es_valida = True

        # Valido que sean numericos
        if not dia.isnumeric() or not mes.isnumeric() or not año.isnumeric():
            fecha_es_valida = False
        # Valido que el dia y el mes no tengan mas de dos ni menos de un digito
        if len(dia) < 1 or len(dia) > 2:
            fecha_es_valida = False
        if len(mes) < 1 or len(mes) > 2:
            fecha_es_valida = False
        # Valido que el año tenga 4 digitos
        if len(año) != 4:
            fecha_es_valida = False
        
        fecha = date(int(año), int(mes), int(dia))

        # Verifico que la fecha no sea posterior a hoy
        if fecha > date.today():
            fecha_es_valida = False

        # Si el dia, el mes o el año no es valido lanzo la excepción
        if not fecha_es_valida:
            raise DatosInvalidos(mensaje_error)

        self._fecha_nacimiento = fecha

    @property
    def edad(self):
        # Obtengo la fecha de hoy
        fecha_actual = date.today()
        # Saco la diferencia de dias restando la fecha actual con la fecha de nacimiento
        diferencia_dias = fecha_actual - self._fecha_nacimiento
        # Divido esa cantidad de dias en 365 para obtener los años
        edad = int(diferencia_dias / timedelta(days=365))
        return edad
    
    @property
    def experiencia(self):
        return self._experiencia

    def validar_y_guardar_experiencia(self, exp: str):
        mensaje_error = "La experiencia es invalida, debe ser un numero menor a la edad"
        if not exp.isnumeric() or int(exp) > self.edad:
            raise DatosInvalidos(mensaje_error)
        self._experiencia = int(exp)

    @property
    def rol(self):
        rol = "Ninguno"
        for id_rol, nombre_rol in self.roles_permitidos:
            if id_rol == self._rol:
                rol = nombre_rol
                break
        return rol
    
    def validar_y_guardar_rol(self, rol_ingresado: str):
        mensaje_error = "El rol ingresado es inválido, ingrese un número de la lista"
        if not rol_ingresado.isnumeric():
            raise DatosInvalidos(mensaje_error)

        # Busco si existe el rol ingresado
        rol = None
        for id_rol, nombre_rol in self.roles_permitidos:
            if id_rol == int(rol_ingresado):
                rol = (id_rol, nombre_rol)
                break
        if not rol:
            raise DatosInvalidos(mensaje_error)
        self._rol = int(rol_ingresado)

    def menu_de_alta(self):
        menu = menu_alta_desarrollador

        """ Cedula """
        print(menu)
        string_ci = "Ingrese cédula (sin puntos ni guiónes):"
        pedir_dato(self.validar_y_guardar_ci,
                   string_ci)
        menu = f"{menu}\n|  Cédula de identidad: {self.ci}"

        """ Nombre """
        print(menu)
        string_nombre = "Ingrese nombre:"
        pedir_dato(self.validar_y_guardar_nombre,
                   string_nombre)
        menu = f"{menu}\n|  Nombre: {self.nombre}"

        """ Apellido """
        print(menu)
        string_apellido = "Ingrese apellido:"
        pedir_dato(self.validar_y_guardar_apellido,
                   string_apellido)
        menu = f"{menu}\n|  Apellido: {self.apellido}"

        """ Pais origen """
        print(menu)
        string_menu_pais = "Seleccione el país de origen\n  " + "\n  ".join([f"{pais[0]} - {pais[1]}" for pais in self.paises_permitidos])
        string_menu_pais += "\n\n  Opcion:"
        pedir_dato(self.validar_y_guardar_pais_origen,
                   string_menu_pais)
        menu = f"{menu}\n|  País de origen: {self.pais_origen}"

        """ Fecha de nacimiento """
        print(menu)
        string_fecha_nacimiento = "Ingrese la fecha de nacimiento (formato: 'DD/MM/YYYY'):"
        pedir_dato(self.validar_y_guardar_fecha_nacimiento,
                   string_fecha_nacimiento)
        menu = f"{menu}\n|  Fecha de nacimiento: {self.fecha_nacimiento}"
        
        """ Experiencia desarrollando """
        print(menu)
        string_experiencia = "Ingrese los años de experiencia (tiene que ser menor a su edad):"
        pedir_dato(self.validar_y_guardar_experiencia,
                   string_experiencia)
        menu = f"{menu}\n|  Años de experiencia: {self.experiencia}"
        
        """ Rol """
        print(menu)
        string_menu_rol = "Seleccione el rol\n  " + "\n  ".join([f"{rol[0]} - {rol[1]}" for rol in self.roles_permitidos])
        string_menu_rol += "\n\n  Opcion:"
        pedir_dato(self.validar_y_guardar_rol,
                   string_menu_rol)
        menu = f"{menu}\n|  Rol: {self.rol}"

        print(menu)
        print("\n\n  ¡Desarrollador dado de alta con éxito!")