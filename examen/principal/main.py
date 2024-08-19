from examen.cliente.main import *
from examen.main import *
from examen.verificaciones.main import *



repetir=True
while repetir:
    opc=0
    while opc<1 or opc>5:
        print ("/////Agencia de autos///")
        print ("----Menu principa----")
        print("""
            Gestionr Autos       [1]
            Gestionar Clientes   [2]
            Gestionar Revisiones [3]
            salir [4]
        """)
        opc=int(input("Ingrese una opcion: "))
    
    if opc==1:
        menu_autos()
    elif opc==2:
        menu_clientes()
    elif opc==3:
        mostrar_menu()
    elif opc==4:
        print("""
                        salir        
        """)
        break