import mysql.connector

#conectar base de datos

conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='escuela'
    
)

#verificar la conexion
if conexion.is_connected():
    print("conexion exitosa")
else:
    print("Conexion fallida")