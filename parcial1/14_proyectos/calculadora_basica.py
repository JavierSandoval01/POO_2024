import os

from funciones_compartir import solicitarDatos,getCalculadora,esperarTecla,solicitarDato

opcion=True
while opcion:
    os.system("clear")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- Potencia \n 6.- Raiz \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    if opcion!="7":
      if opcion=="6" or opcion=="RAIZ":
        n1=solicitarDato()
        n2=0
      else:  
        n1,n2=solicitarDatos()
      print(getCalculadora(n1,n2,opcion))
      esperarTecla()
    else:
      opcion=False
      print("Gracias por utilizar el sistema ...")  
