import mysql.connector

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='mi_empresa',
            user='root',
            password=''
        )
        if conexion.is_connected():
            return conexion
    except:
        print(f"Error al conectar a la base de datos")
        return None