import mysql.connector
try:
    #Conectar con la BD MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='agencia_autos_datos'   
    )
     #Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
    cursor=conexion.cursor(buffered=True)
    
except Exception as e:
    print(f"No fue posible conectar con la BD ... verifique ...")  
else:
    print(f"Se creo la conexion con la BD exitosamente")