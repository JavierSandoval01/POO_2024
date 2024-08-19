from funciones import Revisiones

def mostrar_menu():
    print("=== Menú de Revisiones ===")
    print("1. Insertar revisión")
    print("2. Consultar revisiones")
    print("3. Actualizar revisión")
    print("4. Eliminar revisión")
    print("5. Salir")

def ejecutar_menu():
    revisiones = Revisiones()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            revisiones.insertar()
        elif opcion == '2':
            revisiones.consultar()
        elif opcion == '3':
            revisiones.actualizar()
        elif opcion == '4':
            revisiones.eliminar()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor selecciona otra.")

if __name__ == "__main__":
    ejecutar_menu()
