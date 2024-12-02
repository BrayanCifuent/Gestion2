import mysql.connector
import re

class Usuario:
    def __init__(self, username=None, clave=None, rol_id=None, id_empleado=None):
        """Inicializa un nuevo objeto Usuario con los atributos proporcionados."""
        self.username = username
        self.clave = clave
        self.rol_id = rol_id
        self.id_empleado = id_empleado

    def validar_contrasena(self, contrasena, usuario):
        """Valida que la contraseña cumpla con las reglas de seguridad."""

        # 1. La contraseña debe tener al menos 8 caracteres
        if len(contrasena) < 8:
            print("❌ La contraseña debe tener al menos 8 caracteres.")
            return False

        # 2. La contraseña no debe contener el nombre de usuario
        if usuario.lower() in contrasena.lower():
            print("❌ La contraseña no debe contener el nombre de usuario.")
            return False

        # 3. La contraseña no debe ser igual a contraseñas anteriores
        if self.comprobar_contrasena_anterior(contrasena):
            print("❌ No puede usar contraseñas anteriores.")
            return False

        # 4. No debe usar palabras comunes
        if self.comprobar_palabras_comunes(contrasena):
            print("❌ La contraseña no debe contener palabras del diccionario.")
            return False

        # 5. La contraseña debe contener al menos una letra mayúscula, una minúscula, un número y un símbolo
        if not re.search(r'[A-Z]', contrasena):  # Mayúsculas
            print("❌ La contraseña debe contener al menos una letra mayúscula.")
            return False
        if not re.search(r'[a-z]', contrasena):  # Minúsculas
            print("❌ La contraseña debe contener al menos una letra minúscula.")
            return False
        if not re.search(r'[0-9]', contrasena):  # Números
            print("❌ La contraseña debe contener al menos un número.")
            return False

        # 6. La contraseña debe contener al menos un símbolo no alfanumérico
        if not re.search(r'[^a-zA-Z0-9]', contrasena):  # Símbolos
            print("❌ La contraseña debe contener al menos un símbolo no alfanumérico.")
            return False

        return True  # Si pasa todas las validaciones

    def comprobar_contrasena_anterior(self, contrasena):
        """Simula la comprobación de contraseñas anteriores (esto debería consultar la base de datos)."""
        contraseñas_anteriores = ['password123', '12345678', 'qwerty']
        if contrasena in contraseñas_anteriores:
            return True
        return False

    def comprobar_palabras_comunes(self, contrasena):
        """Simula la comprobación de palabras comunes (esto debería consultar un diccionario real)."""
        palabras_prohibidas = ['contraseña', 'password', '123456', 'admin', 'qwerty']
        if any(palabra in contrasena.lower() for palabra in palabras_prohibidas):
            return True
        return False

    def iniciar_sesion(self):
        """Función para manejar el inicio de sesión del usuario consultando la base de datos."""
        intentos = 3  # Intentos de inicio de sesión
        while intentos > 0:
            self.username = input("Ingrese su nombre de usuario: ")
            self.clave = input("Ingrese su contraseña: ")

            # Conexión a la base de datos
            try:
                conexion = mysql.connector.connect(
                    host='localhost',  # Cambiar a tu servidor MySQL
                    user='root',       # Cambiar a tu usuario MySQL
                    password='',  # Cambiar a tu contraseña MySQL
                    database='gestion_empleados'  # Cambiar a tu base de datos
                )
                cursor = conexion.cursor()

                # Consulta SQL para verificar las credenciales
                query = """ 
                    SELECT u.id_usuario, u.username, u.clave, u.rol_id, u.id_empleado 
                    FROM usuarios u 
                    WHERE u.username = %s AND u.clave = %s
                """
                cursor.execute(query, (self.username, self.clave))

                # Verificar si hay resultados
                resultado = cursor.fetchone()
                if resultado:
                    print(f"Bienvenido al sistema, {resultado[1]} (ID: {resultado[0]})")
                    print(f"Rol ID: {resultado[3]}, Empleado ID: {resultado[4]}")
                    self.id_empleado = resultado[4]  # Asignar el ID del empleado al objeto
                    self.rol_id = resultado[3]  # Asignar el rol al objeto
                    cursor.close()
                    conexion.close()
                    return True  # Inicio de sesión exitoso
                else:
                    intentos -= 1
                    print(f"❌ Credenciales incorrectas. Te quedan {intentos} intentos.")
                    cursor.close()
                    conexion.close()

            except mysql.connector.Error as err:
                print(f"❌ Error de conexión a la base de datos: {err}")
                return False

        print("❌ Se han agotado los intentos. Saliendo del sistema...")
        return False  # Si se agotaron los intentos

    def agregar_usuario(self):
        """Función para agregar un nuevo usuario a la base de datos."""
        print("=== Agregar Nuevo Usuario ===")

        # Validar rol y ID de empleado
        while True:
            try:
                self.rol_id = int(input("Ingrese el rol"
                                        "1)(Administrador General"
                                        "2)Administrador Comercial"
                                        "4)Gerente de Área"
                                        "5Técnico"
                                        "5)Operario."))
                if self.rol_id not in [1, 2, 3, 4, 5]:  
                    print("❌ El rol debe ser 1 (Administrador General) o 2 (Administrador Comercial) o 3 (Gerente de Área) o 4 (Técnico) o 5 (Operario).")
                else:
                    break
            except ValueError:
                print("❌ Debe ingresar un número válido para el rol.")

        # Aquí se asocia el username con el ID del empleado
        self.id_empleado = input("Ingrese el ID del empleado: ")
        self.username = self.id_empleado  # Asignamos el ID del empleado como nombre de usuario

        # Validar la contraseña
        while True:
            self.clave = input("Ingrese la contraseña: ")
            if self.validar_contrasena(self.clave, self.username):
                break
            else:
                print("❌ La contraseña no es válida. Intente nuevamente.")

        # Conexión a la base de datos
        try:
            conexion = mysql.connector.connect(
                host='localhost',  # Cambiar a tu servidor MySQL
                user='root',       # Cambiar a tu usuario MySQL
                password='',  # Cambiar a tu contraseña MySQL
                database='gestion_empleados'  # Cambiar a tu base de datos
            )
            cursor = conexion.cursor()

            # Consulta SQL para agregar el nuevo usuario
            query = """
                INSERT INTO usuarios (username, clave, rol_id, id_empleado) 
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (self.username, self.clave, self.rol_id, self.id_empleado))
            conexion.commit()  # Confirmar la inserción

            print(f"✔️ Usuario '{self.username}' agregado exitosamente.")
            cursor.close()
            conexion.close()

        except mysql.connector.Error as err:
            print(f"❌ Error al agregar el usuario a la base de datos: {err}")

# Función para el menú principal


