#ejemplo 5 Crear un programa que permita Gestionar (Administrar) peliculas, colocar un menu de opciones para agregar, remover, consultar peliculas. 
#Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar listas para almacenar los nombres de peliculas  

from funciones_compartir import borrarPantalla,agregarPeliculas,eliminarPeliculas,actualizarPeliculas,consultarPeliculas,buscarPeliculas,esperarTecla,vaciarPeliculas


opcion=True 

while opcion:
 borrarPantalla()
 print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
 opcion=input("\t Elige una opción: ").upper()
 
 if opcion!="7":
  if opcion=="1":
    agregarPeliculas()
  elif opcion=="2":
    eliminarPeliculas() 
  elif opcion=="3":
    actualizarPeliculas()  
  elif opcion=="4":
    consultarPeliculas()  
  elif opcion=="5":
    buscarPeliculas() 
  elif opcion=="6":
    print(vaciarPeliculas())  
  else:
    print("Opción invalida vuelva a intentarlo ... por favor")  
  esperarTecla()      
 else:  
  opcion=False    
  print("Terminaste la ejecucion del SW") 
 
 