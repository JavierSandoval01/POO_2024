def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")
        
def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\n \t \tOprima cualquier tecla para continuar ...")
  input()  