import mysql.connector

# Conectar a MySQL
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",  
        password=""  
    )

    mycursor = mydb.cursor()

    # Crear base de datos
    mycursor.execute("CREATE DATABASE IF NOT EXISTS `gestion_empleados`")
    mycursor.execute("USE `gestion_empleados`")

    # Crear tablas
    mycursor.execute(""" 
    CREATE TABLE IF NOT EXISTS `departamentos` (
        `id_departamento` INT(20) NOT NULL PRIMARY KEY,
        `nombre_departamentos` VARCHAR(30) NOT NULL,
        `telefono` INT(10) NOT NULL,
        `habilitado` TINYINT(1) NOT NULL DEFAULT 1
    ) 
    """)

    mycursor.execute(""" 
    CREATE TABLE IF NOT EXISTS `tipo_empleados` (
        `Id_tipo_empleado` INT(20) NOT NULL PRIMARY KEY,
        `nombre_tipo` VARCHAR(20) NOT NULL,
        `detalle` VARCHAR(50) NOT NULL
    ) 
    """)

    mycursor.execute(""" 
    CREATE TABLE IF NOT EXISTS `empleado` (
        `id_empleado` INT(20) NOT NULL PRIMARY KEY,
        `nombre` VARCHAR(20) NOT NULL,
        `direccion` VARCHAR(30) NOT NULL,
        `telefono` INT(20) NOT NULL,
        `correo` VARCHAR(20) NOT NULL,
        `fecha_inicio` VARCHAR(20) NOT NULL,
        `salario` INT(20) NOT NULL,
        `id_tipo` INT(20) NOT NULL,
        `id_departamento` INT(20) NOT NULL,
        `habilitado` TINYINT(4) NOT NULL DEFAULT 1,
        FOREIGN KEY (`id_departamento`) REFERENCES departamentos(`id_departamento`),
        FOREIGN KEY (`id_tipo`) REFERENCES tipo_empleados(`Id_tipo_empleado`)
    ) 
    """)

    mycursor.execute(""" 
    CREATE TABLE IF NOT EXISTS `proyectos` (
        `Id_proyecto` INT(20) NOT NULL PRIMARY KEY,
        `nombre_proyecto` VARCHAR(25) NOT NULL,
        `descripcion` VARCHAR(50) NOT NULL,
        `Fecha_inicio` VARCHAR(20) NOT NULL,
        `habilitado` TINYINT(1) NOT NULL DEFAULT 1
    ) 
    """)

    mycursor.execute(""" 
    CREATE TABLE IF NOT EXISTS `proyectoempleado` (
        `id_asociacion` INT(20) NOT NULL PRIMARY KEY,
        `id_proyecto` INT(20) NOT NULL,
        `id_empleado` INT(20) NOT NULL,
        FOREIGN KEY (`id_proyecto`) REFERENCES proyectos(`Id_proyecto`),
        FOREIGN KEY (`id_empleado`) REFERENCES empleado(`id_empleado`)
    )
    """)

    mycursor.execute(""" 
    CREATE TABLE IF NOT EXISTS `registrartiempo` (
        `id_registrar` INT(200) NOT NULL PRIMARY KEY,
        `id_empleado` INT(20) NOT NULL,
        `fecha` VARCHAR(20) NOT NULL,
        `horas` INT(20) NOT NULL,
        `tareas` VARCHAR(60) NOT NULL,
        `id_proyecto` INT(20) DEFAULT NULL,
        FOREIGN KEY (`id_empleado`) REFERENCES empleado(`id_empleado`),
        FOREIGN KEY (`id_proyecto`) REFERENCES proyectos(`Id_proyecto`)
    )
    """)

    mycursor.execute(""" 
    CREATE TABLE IF NOT EXISTS `roles` (
        `id` INT(11) NOT NULL PRIMARY KEY,
        `nombre` VARCHAR(50) NOT NULL,
        `descripcion_rol` VARCHAR(255) NOT NULL,  
        `permisos_rol` VARCHAR(255) NOT NULL,     
        `habilitado` TINYINT(1) NOT NULL DEFAULT 1 
    )
    """)

    mycursor.execute(""" 
    CREATE TABLE IF NOT EXISTS `usuarios` (
        `id_usuario` INT(200) NOT NULL PRIMARY KEY,
        `username` VARCHAR(200) NOT NULL,
        `clave` VARCHAR(200) NOT NULL,
        `rol_id` INT(11) DEFAULT NULL,
        `id_empleado` INT(11) DEFAULT NULL,
        FOREIGN KEY (`rol_id`) REFERENCES roles(`id`),
        FOREIGN KEY (`id_empleado`) REFERENCES empleado(`id_empleado`)
    ) 
    """)

        # Datos a insertar
    departamentos = [
        (0, 'Departamento de Recursos Human', 5550101, 1),
        (2, 'Finanzas', 5550103, 1),
        (3, 'Departamento de marketing', 5550105, 1),
        (4, 'Departamento de IT', 5550106, 1),
        (6, 'Departamento de ventas', 5530108, 1),
        (213, 'Marketing', 987656354, 1)
    ]

    tipo_empleados = [
        (0, 'Administrativo', 'Encargado de tareas administrativas y gestión de datos.'),
        (203, 'Técnico', 'Especialista en mantenimiento y soporte técnico.'),
        (303, 'Vendedor', 'Responsable de la atención al cliente y cierre de ventas.'),
        (404, 'Gerente', 'Encargado de supervisar equipos y tomar decisiones.'),
        (505, 'Diseñador', 'Creativo responsable de la estética y diseño de proyectos.'),
        (606, 'Analista', 'Encargado de analizar datos y generar informes para la toma de decisiones.'),
        (777, 'Consultor', 'Proporciona asesoramiento especializado a clientes.'),
        (808, 'Recursos Humanos', 'Encargado de la gestión del talento humano y procesos de selección.'),
        (909, 'Financiero', 'Responsable de la gestión financiera y presupuesto.'),
        (1101, 'Marketing', 'Encargado de la promoción y publicidad de productos.'),
        (2024, 'Diseñadores de Producto', 'Se encargan de la estética y funcionalidad de productos.'),
    ]

    empleados = [
        (111, 'Juan Perez', 'AV Alemania 204, Temuco', 55678922, 'juan20@gmail.com', '2023-01-15', 300000, 404, 0, 1),
        (222, 'María López', 'Gral Pinto Puelma 29', 55677933, 'maria33@gmail.com', '2023-02-20', 450000, 606, 2, 1),
        (2121, 'Gerardo', 'Nose21', 123456788, 'gerardo@gmail.com', '2020-02-21', 200000, 0, 3, 1),
        (13254345, 'Agustin', 'Leon Gallo 345, Temuco', 978563732, 'agustin@gmail.com', '2024-07-09', 800000, 203, 4, 1),
        (21299226, 'Brayan', 'Pedro de Valdivia 782, Villarri', 9978321, 'brayan@gmail.com', '2003-05-08', 6003213, 505, 6, 1),
        (87656876, 'Tomas', 'Leon Gallo 763', 965748765, 'tomas@gmail.com', '2024-03-05', 700000, 303, 213, 1),
        (333, 'Lucía Fernández', 'Calle Falsa 123', 5550123, 'lucia@gmail.com', '2024-01-10', 450000, 808, 0, 1),
        (444, 'Carlos Gómez', 'Calle Verdadera 456', 5550456, 'carlos@gmail.com', '2023-11-05', 600000, 909, 2, 1),
        (555, 'Ana Torres', 'Calle Real 789', 5550789, 'ana@gmail.com', '2024-02-15', 700000, 1101, 4, 1),
        (666, 'Pedro Sánchez', 'Calle Principal 10', 5550100, 'pedro@gmail.com', '2023-09-20', 800000, 203, 6, 1),
        (777, 'Sofia Ruiz', 'Calle Secundaria 11', 5550111, 'sofia@gmail.com', '2023-12-01', 900000, 404, 0, 1),
    ]

    proyectos = [
        (1, 'Edificios', '50 edificios', '2020-04-05', 1),
        (3, 'Condominio', '50 casas y 2 departamentos', '2024-10-10', 1),
        (23, 'Casas', '100 casas en la región', '2021-08-01', 1)
    ]

    proyecto_empleado = [
        (1, 1, 111),      # Juan Perez en proyecto 1 (Edificios)
        (2, 1, 222),      # María López en proyecto 1 (Edificios)
        (3, 1, 333),      # Lucía Fernández en proyecto 1 (Edificios)
        (4, 3, 2121),     # Gerardo en proyecto 3 (Condominio)
        (5, 3, 21299226), # Brayan en proyecto 3 (Condominio)
        (6, 3, 444),      # Carlos Gómez en proyecto 3 (Condominio)
        (7, 23, 13254345), # Agustin en proyecto 23 (Casas)
        (8, 23, 87656876), # Tomas en proyecto 23 (Casas)
        (9, 23, 666),      # Pedro Sánchez en proyecto 23 (Casas)
        (10, 23, 777)      # Sofia Ruiz en proyecto 23 (Casas)
    ]

    registrartiempo = [
        (1, 111, '2024-10-01', 8, 'Desarrollo de software', 1),
        (2, 222, '2024-10-02', 7, 'Análisis financiero', 3),
        (3, 2121, '2024-10-03', 6, 'Mantenimiento de sistemas', 23),
        (4, 13254345, '2024-10-04', 5, 'Diseño de prototipos', 1),
        (5, 21299226, '2024-10-05', 8, 'Diseño gráfico', 1),
        (6, 87656876, '2024-10-06', 6, 'Ventas de marketing', 3),
        (7, 333, '2024-10-07', 7, 'Reclutamiento', 23),
        (8, 444, '2024-10-08', 5, 'Contabilidad', 1),
        (9, 555, '2024-10-09', 6, 'Estrategia de marketing', 1),
        (10, 666, '2024-10-10', 4, 'Soporte técnico', 3),
        (11, 777, '2024-10-11', 8, 'Liderazgo de equipo', 23),
        (12, 111, '2024-10-12', 7, 'Evaluación de desempeño', 1),
        (13, 222, '2024-10-13', 5, 'Elaboración de informes', 3),
        (14, 2121, '2024-10-14', 6, 'Coordinación de eventos', 23),
        (15, 13254345, '2024-10-15', 5, 'Implementación de nuevas tecnologías', 1),
        (16, 21299226, '2024-10-16', 8, 'Investigación de mercado', 1),
        (17, 87656876, '2024-10-17', 5, 'Atención al cliente', 3),
        (18, 333, '2024-10-18', 7, 'Planificación estratégica', 23),
        (19, 444, '2024-10-19', 6, 'Auditoría financiera', 1),
        (20, 555, '2024-10-20', 5, 'Desarrollo de contenido', 1),
        (21, 666, '2024-10-21', 8, 'Optimización de procesos', 3),
        (22, 777, '2024-10-22', 7, 'Coaching de equipo', 23)
    ]


    roles = [
        (1, 'Administradir General', 'Administrador con permisos completos sobre el sistema', 'Puede hacer todo', 1),
        (2, 'Aministrador Comercial', 'control comercial', 'Ver perfil, Editar perfil, Ver proyectos asignados', 1),
        (3, 'Gerete de Area', 'Rol con permisos para gestionar proyectos y supervisar empleados', 'Ver proyectos, Asignar empleados, Editar proyectos, Ver reportes', 1),
        (4, 'Tecnico', 'Registrar horas de trabajo y informes de proyectos', 'Registra su tiempo y informes de proyectos', 1),
        (5, 'Operario', 'Rol basico, solo registra tiempo', 'Registra su tiempo', 1)
    ]

    usuarios = [
        (1, 'admin', '1234', 1, 111),
        (2, 'user1', '12345', 2, 222),
        (3, 'user2', '123456', 2, 2121),
        (4, 'gerente1', '123456', 3, 13254345)
    ]

    # Insertar datos en departamentos
    for departamento in departamentos:
        mycursor.execute("SELECT COUNT(*) FROM departamentos WHERE id_departamento = %s", (departamento[0],))
        exists = mycursor.fetchone()[0]

        if exists == 0:
            mycursor.execute("INSERT INTO departamentos (id_departamento, nombre_departamentos, telefono, habilitado) VALUES (%s, %s, %s, %s)", departamento)
            print(f"Departamento {departamento[1]} insertado correctamente.")
            mydb.commit()  # Commit para confirmar la inserción
        else:
            print(f"Departamento con id {departamento[0]} ya existe, no se insertó.")

    # Insertar datos en tipo_empleados
    for tipo in tipo_empleados:
        mycursor.execute("SELECT COUNT(*) FROM tipo_empleados WHERE Id_tipo_empleado = %s", (tipo[0],))
        exists = mycursor.fetchone()[0]

        if exists == 0:
            mycursor.execute("INSERT INTO tipo_empleados (Id_tipo_empleado, nombre_tipo, detalle) VALUES (%s, %s, %s)", tipo)
            print(f"Tipo de empleado {tipo[1]} insertado correctamente.")
            mydb.commit()
        else:
            print(f"Tipo de empleado con id {tipo[0]} ya existe, no se insertó.")

    # Insertar datos en empleados
    for empleado in empleados:
        mycursor.execute("SELECT COUNT(*) FROM empleado WHERE id_empleado = %s", (empleado[0],))
        exists = mycursor.fetchone()[0]

        if exists == 0:
            mycursor.execute("""
                INSERT INTO empleado (id_empleado, nombre, direccion, telefono, correo, fecha_inicio, salario, id_tipo, id_departamento, habilitado) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, empleado)
            print(f"Empleado {empleado[1]} insertado correctamente.")
            mydb.commit()
        else:
            print(f"Empleado con id {empleado[0]} ya existe, no se insertó.")

    # Insertar datos en proyectos
    for proyecto in proyectos:
        mycursor.execute("SELECT COUNT(*) FROM proyectos WHERE Id_proyecto = %s", (proyecto[0],))
        exists = mycursor.fetchone()[0]

        if exists == 0:
            mycursor.execute("INSERT INTO proyectos (Id_proyecto, nombre_proyecto, descripcion, Fecha_inicio, habilitado) VALUES (%s, %s, %s, %s, %s)", proyecto)
            print(f"Proyecto {proyecto[1]} insertado correctamente.")
            mydb.commit()
        else:
            print(f"Proyecto con id {proyecto[0]} ya existe, no se insertó.")

    # Insertar datos en proyectoempleado
    for asociacion in proyecto_empleado:
        mycursor.execute("SELECT COUNT(*) FROM proyectoempleado WHERE id_proyecto = %s AND id_empleado = %s", (asociacion[1], asociacion[2]))
        exists = mycursor.fetchone()[0]

        if exists == 0:
            mycursor.execute("INSERT INTO proyectoempleado (id_asociacion, id_proyecto, id_empleado) VALUES (%s, %s, %s)", asociacion)
            print(f"Asociación Proyecto-Empleado {asociacion[0]} insertada correctamente.")
            mydb.commit()
        else:
            print(f"Asociación Proyecto-Empleado con id_proyecto {asociacion[1]} y id_empleado {asociacion[2]} ya existe, no se insertó.")

    # Insertar datos en registrartiempo
    for registro in registrartiempo:
        mycursor.execute("SELECT COUNT(*) FROM registrartiempo WHERE id_registrar = %s", (registro[0],))
        exists = mycursor.fetchone()[0]

        if exists == 0:
            mycursor.execute("INSERT INTO registrartiempo (id_registrar, id_empleado, fecha, horas, tareas, id_proyecto) VALUES (%s, %s, %s, %s, %s, %s)", registro)
            print(f"Registro de tiempo {registro[0]} insertado correctamente.")
            mydb.commit()
        else:
            print(f"Registro de tiempo con id_registrar {registro[0]} ya existe, no se insertó.")

    # Insertar datos en roles
    for rol in roles:
        # Verificar si el rol ya existe en la base de datos
        mycursor.execute("SELECT COUNT(*) FROM roles WHERE id = %s", (rol[0],))
        exists = mycursor.fetchone()[0]

        if exists == 0:
            # Si el rol no existe, insertamos los valores. Asumimos que `id` es auto-incremental.
            # Aquí `rol[1]` es el nombre, `rol[2]` es descripcion_rol, `rol[3]` son permisos_rol, y `rol[4]` es habilitado
            mycursor.execute("""
                INSERT INTO roles (id, nombre, descripcion_rol, permisos_rol, habilitado)
                VALUES (%s, %s, %s, %s, %s)
            """, (rol[0], rol[1], rol[2], rol[3], rol[4]))
            print(f"Rol {rol[1]} insertado correctamente.")
            mydb.commit()
        else:
            print(f"Rol con id {rol[0]} ya existe, no se insertó.")

    # Insertar datos en usuarios
    for usuario in usuarios:
        mycursor.execute("SELECT COUNT(*) FROM usuarios WHERE id_usuario = %s", (usuario[0],))
        exists = mycursor.fetchone()[0]

        if exists == 0:
            mycursor.execute("INSERT INTO usuarios (id_usuario, username, clave, rol_id, id_empleado) VALUES (%s, %s, %s, %s, %s)", usuario)
            print(f"Usuario {usuario[1]} insertado correctamente.")
            mydb.commit()
        else:
            print(f"Usuario con id_usuario {usuario[0]} ya existe, no se insertó.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if mycursor:
        mycursor.close()
    if mydb:
        mydb.close()