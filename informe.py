import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "gestion_empleados"
)
print(mydb)

class Informe:
    def __init__(self, id_proyecto, id_empleado, id_depto, id_registrado):
        self.id_proyecto = id_proyecto
        self.id_empleado = id_empleado
        self.id_depto = id_depto
        self.id_registrado = id_registrado

    def generar_informe(self):
        return f"Informe:\nID Proyecto: {self.id_proyecto}\nID Empleado: {self.id_empleado}\nID Departamento: {self.id_depto}\nID Registrado: {self.id_registrado}"

    def exportar_informe(self, filename):
        with open(filename, 'w') as file:
            file.write(self.generar_informe())
        print(f"Informe exportado a {filename}")