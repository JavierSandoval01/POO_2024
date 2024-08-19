from conexionBD import *
def actualizar_auto():
    try:
        # Mostrar todos los autos actuales
        query = "SELECT * FROM autos"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)

        # Solicitar al usuario la matrícula del auto que desea actualizar
        mat = input("Ingrese la matrícula del auto a actualizar: ")

        # Solicitar nuevos datos al usuario
        matricula = input("Ingrese la nueva matricula: ")
        marca = input("Ingrese la nueva marca: ")
        modelo = input("Ingrese el nuevo modelo: ")
        color = input("Ingrese el nuevo color: ")
        nif = input("Ingrese el nuevo nif: ")

        # Confirmar la actualización
        print(f"Estas seguro de actualizar el registro de la matrícula {mat}?")
        confirmar = input("Escriba \"ACTUALIZAR\" para confirmar o \"CANCELAR\" para cancelar: ").upper()

        if confirmar == "ACTUALIZAR":
            # Actualizar el registro con los nuevos datos
            sql = "UPDATE autos SET matricula = %s, marca = %s, modelo = %s, color = %s, nif=%s WHERE matricula = %s"
            cursor.execute(sql, (matricula, marca, modelo, color, nif))
            conexion.commit()
            print("Registro actualizado correctamente")
        else:
            print("Actualización del registro cancelada")

    except Exception as e:
        print(f"Ocurrió un error con el servidor...por favor intente más tarde. Error: {e}")

    else:
        print("Ejecución realizada correctamente")
