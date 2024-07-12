from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="delete from clientes where id=1"

    micursor.execute(sql)
    conexion.commit()

except:
    print(f"Ocurrio un error con el servidor")

else:
    print(f"Registro insertado correctamente")