from entities.Desarrollador import Desarrollador


# Diseñador 1
disenador_1 = Desarrollador()
disenador_1.validar_y_guardar_ci("54196160")
disenador_1.validar_y_guardar_nombre("Lucas")
disenador_1.validar_y_guardar_apellido("Pintos")
disenador_1.validar_y_guardar_pais_origen("4")
disenador_1.validar_y_guardar_fecha_nacimiento("14/05/2000")
disenador_1.validar_y_guardar_experiencia("1")
disenador_1.validar_y_guardar_rol("1")

# Diseñador 2
disenador_2 = Desarrollador()
disenador_2.validar_y_guardar_ci("58493850")
disenador_2.validar_y_guardar_nombre("Gonzalo")
disenador_2.validar_y_guardar_apellido("Perez")
disenador_2.validar_y_guardar_pais_origen("2")
disenador_2.validar_y_guardar_fecha_nacimiento("14/05/2001")
disenador_2.validar_y_guardar_experiencia("4")
disenador_2.validar_y_guardar_rol("1")


# Productor 1
productor = Desarrollador()
productor.validar_y_guardar_ci("33759488")
productor.validar_y_guardar_nombre("Cinthya")
productor.validar_y_guardar_apellido("Belvisi")
productor.validar_y_guardar_pais_origen("2")
productor.validar_y_guardar_fecha_nacimiento("14/10/2001")
productor.validar_y_guardar_experiencia("4")
productor.validar_y_guardar_rol("2")


# Programador 1
programador_1 = Desarrollador()
programador_1.validar_y_guardar_ci("35748294")
programador_1.validar_y_guardar_nombre("Jorge")
programador_1.validar_y_guardar_apellido("Pintos")
programador_1.validar_y_guardar_pais_origen("4")
programador_1.validar_y_guardar_fecha_nacimiento("21/08/2001")
programador_1.validar_y_guardar_experiencia("4")
programador_1.validar_y_guardar_rol("3")


# Programador 2
programador_2 = Desarrollador()
programador_2.validar_y_guardar_ci("31365748")
programador_2.validar_y_guardar_nombre("Santiago")
programador_2.validar_y_guardar_apellido("Ramirez")
programador_2.validar_y_guardar_pais_origen("1")
programador_2.validar_y_guardar_fecha_nacimiento("28/02/1997")
programador_2.validar_y_guardar_experiencia("8")
programador_2.validar_y_guardar_rol("3")


# Programador 3
programador_3 = Desarrollador()
programador_3.validar_y_guardar_ci("38758491")
programador_3.validar_y_guardar_nombre("Gustavo")
programador_3.validar_y_guardar_apellido("Mendez")
programador_3.validar_y_guardar_pais_origen("3")
programador_3.validar_y_guardar_fecha_nacimiento("10/02/1998")
programador_3.validar_y_guardar_experiencia("4")
programador_3.validar_y_guardar_rol("3")

# Programador 3
programador_4 = Desarrollador()
programador_4.validar_y_guardar_ci("52650714")
programador_4.validar_y_guardar_nombre("Lpintos")
programador_4.validar_y_guardar_apellido("Lpintos")
programador_4.validar_y_guardar_pais_origen("2")
programador_4.validar_y_guardar_fecha_nacimiento("06/12/2002")
programador_4.validar_y_guardar_experiencia("7")
programador_4.validar_y_guardar_rol("3")

# Programador 3
programador_5 = Desarrollador()
programador_5.validar_y_guardar_ci("52650711")
programador_5.validar_y_guardar_nombre("Lmateo")
programador_5.validar_y_guardar_apellido("Lmateo")
programador_5.validar_y_guardar_pais_origen("1")
programador_5.validar_y_guardar_fecha_nacimiento("07/12/2001")
programador_5.validar_y_guardar_experiencia("6")
programador_5.validar_y_guardar_rol("3")

# Programador 3
programador_6 = Desarrollador()
programador_6.validar_y_guardar_ci("52650715")
programador_6.validar_y_guardar_nombre("Libanes")
programador_6.validar_y_guardar_apellido("Libanes")
programador_6.validar_y_guardar_pais_origen("3")
programador_6.validar_y_guardar_fecha_nacimiento("08/12/2002")
programador_6.validar_y_guardar_experiencia("9")
programador_6.validar_y_guardar_rol("3")


# Tester 1
tester_1 = Desarrollador()
tester_1.validar_y_guardar_ci("37489389")
tester_1.validar_y_guardar_nombre("Luciano")
tester_1.validar_y_guardar_apellido("Alcaeida")
tester_1.validar_y_guardar_pais_origen("1")
tester_1.validar_y_guardar_fecha_nacimiento("10/02/2001")
tester_1.validar_y_guardar_experiencia("3")
tester_1.validar_y_guardar_rol("4")

# Tester 2
tester_2 = Desarrollador()
tester_2.validar_y_guardar_ci("37876568")
tester_2.validar_y_guardar_nombre("Ramiro")
tester_2.validar_y_guardar_apellido("Hernandez")
tester_2.validar_y_guardar_pais_origen("2")
tester_2.validar_y_guardar_fecha_nacimiento("10/02/2001")
tester_2.validar_y_guardar_experiencia("3")
tester_2.validar_y_guardar_rol("4")


# Tester 2
tester_3 = Desarrollador()
tester_3.validar_y_guardar_ci("37876566")
tester_3.validar_y_guardar_nombre("Ramiro")
tester_3.validar_y_guardar_apellido("Pepe")
tester_3.validar_y_guardar_pais_origen("2")
tester_3.validar_y_guardar_fecha_nacimiento("11/02/2001")
tester_3.validar_y_guardar_experiencia("1")
tester_3.validar_y_guardar_rol("4")

desarrolladores_prueba = [disenador_1, disenador_2, productor,
                          programador_1, programador_2, programador_3, programador_4, programador_5, programador_6, tester_1, tester_2, tester_3]
