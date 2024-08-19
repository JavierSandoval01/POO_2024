from conexionBD import *
from gestion.insertar import *
from gestion.consultar import *
from gestion.eliminar import *
from gestion.actualizar import *


def menu_autos():
    repetir = True
    while repetir:
        opc = 0
        while opc < 1 or opc > 5:
            print("/////Agencia de autos///")
            print("----Menu principal----")
            print("""
                Insertar autos   [1]
                Consultar autos  [2]
                Eliminar autos   [3]
                Actualizar autos [4]
                Salir [5]
            """)
            opc = int(input("Ingrese una opción: "))
        
        if opc == 1:
            print("""
                            INSERTAR DATOS DE AUTOS 
                            Ingrese los datos del auto
            """)
            matricula = input("Ingrese la matrícula del auto a registrar: ")
            marca = input("Ingrese la marca del auto a registrar: ")
            modelo = input("Ingrese el modelo del auto a registrar: ")
            color = input("Ingrese el color del auto a registrar: ")
            nif = input("Ingrese el NIF del auto a registrar: ")
            
            obj_persona = insertar(matricula, marca, modelo, color, nif)
            resultado = obj_persona.registrarauto()
        
        elif opc == 2:
            print("""
                            CONSULTAR DATOS DE AUTOS        
            """)
            consultar()
        elif opc == 3:
            print("""
                            ELIMINAR DATOS DE AUTOS        
            """)
            eliminiar_auto()
        elif opc == 4:
            print("""
                            ACTUALIZAR DATOS        
            """)
            actualizar_auto()
        elif opc == 5:
            print("""
                            Salir        
            """)
            break
