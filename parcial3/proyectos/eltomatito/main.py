import mysql.connector

# Configuración de la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eltomatito2"
)

cursor = conexion.cursor()

# Función para mostrar el menú de una categoría específica
def mostrar_menu(tabla):
    if tabla == "Tacos":
        query = "SELECT id_taco, guiso, precio FROM Tacos"
    elif tabla == "Burros":
        query = "SELECT id_burro, guiso, precio FROM Burros"
    elif tabla == "Chonchos":
        query = "SELECT id_choncho, guiso, precio FROM Chonchos"
    elif tabla == "Campechanos":
        query = "SELECT id_campechano, guiso, precio FROM Campechanos"
    elif tabla == "Aguas":
        query = "SELECT id_agua, sabor, precio FROM Aguas"
    elif tabla == "OtrasBebidas":
        query = "SELECT id_bebida, nombre, precio FROM OtrasBebidas"
    else:
        query = None

    if query:
        cursor.execute(query)
        return cursor.fetchall()
    else:
        return []

# Función para tomar la orden
def tomar_orden():
    print('Ingrese el número de mesa a tomar la orden:')
    num_mesa = int(input())
    print('Ingrese el número de personas:')
    num_personas = int(input())

    print('                    -->TOMAR LA ORDEN<--')
    ordenes = []

    categorias = {
        'A': 'Tacos',
        'B': 'Burros',
        'C': 'Chonchos',
        'D': 'Campechanos',
        'E': 'Aguas',
        'F': 'OtrasBebidas'
    }

    while True:
        print('                    -->Lista de menús<--')
        print('Seleccione la letra de acuerdo a la categoría de menú que corresponda:')
        print('[A] Tacos [B] Burros [C] Chonchos [D] Campechanos [E] Bebidas [F] Otras Bebidas')
        print('[X] Para terminar pedido')
        categoria = input('Seleccione una opción: ').upper()

        if categoria == 'X':
            break

        if categoria in categorias:
            platillos = mostrar_menu(categorias[categoria])
            print(f"Menú de {categorias[categoria]}:")
            for platillo in platillos:
                print(f"{platillo[0]} - {platillo[1]}: ${platillo[2]}")
            
            id_platillo = int(input('Ingrese el ID del platillo que desea: '))
            cantidad = int(input('Ingrese la cantidad: '))
            ordenes.append((id_platillo, categorias[categoria], cantidad))
        else:
            print("Opción no válida. Intente nuevamente.")

    print("Resumen del pedido:")
    for orden in ordenes:
        print(f"{orden[1]}: {orden[0]} - Cantidad: {orden[2]}")

    # Guardar el pedido en la base de datos
    try:
        # Inserción en la tabla Pedido
        cursor.execute(
            "INSERT INTO Pedido (numeroMesa, numeroPersonas, id_cliente, id_mesero) VALUES (%s, %s, %s, %s)",
            (num_mesa, num_personas, 1, 1)  # Supongamos id_cliente = 1 y id_mesero = 1
        )
        id_pedido = cursor.lastrowid

        # Inserción en la tabla Pedido_Detalle
        for id_platillo, tipo_platillo, cantidad in ordenes:
            cursor.execute(
                "INSERT INTO Pedido_Detalle (id_pedido, id_platillo, tipo_platillo, cantidad) VALUES (%s, %s, %s, %s)",
                (id_pedido, id_platillo, tipo_platillo, cantidad)
            )

        conexion.commit()
        print("Pedido guardado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conexion.rollback()

if __name__ == "__main__":
    tomar_orden()

    cursor.close()
    conexion.close()
