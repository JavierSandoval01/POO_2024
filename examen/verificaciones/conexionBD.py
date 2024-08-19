import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',  
        password='',  
        database='agencia_autos_datos'
    )
    return conexion
