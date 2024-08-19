from conexionBD import *

def consultar():
    try:
        micursor=conexion.cursor()

        sql="select matricula,marca,modelo,color,nif from autos"
        micursor.execute(sql)
        resultado=micursor.fetchall()

        if len(resultado)>0:
            print(f"Registros de la tabla: {len(resultado)}")
            for x in resultado:
                print("|matricula|marca|modelo|color|nif|")
                print(x)
    except:
        print(f"Ocurrio un error con el servidor...por favor intente mas tarde")

    else:
        print(f"Registro consultado correctamente")