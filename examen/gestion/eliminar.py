from conexionBD import *

def eliminiar_auto():
    try:
        query = "SELECT * FROM autos"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
         print(fila)
        micursor=conexion.cursor()
        
        
        
        mat =input("Ingrese la matricula del auto a eliminar: ")
        # Mostrar los datos actuales del libro
        
        print(f"Estas seguro de eliminar el registro:")
        confirmar=input("Escriba \"ELIMINAR\" para eliminar el registro o escriba \"CANCELAR\" para no eliminarlo: ").upper()
   
        if confirmar=="ELIMINAR":
            sql = "delete FROM autos WHERE matricula = %s"
            micursor.execute(sql, (mat,))
            resultado = micursor.fetchone()
            conexion.commit()
            print("Registro eliminado correctamente")
        else:
            print("Eliminación del registro cancelado")

    except:
        print(f"Ocurrio un error con el servidor...por favor intente mas tarde")

    else:
        print(f"Ejecución realizada correctamente")