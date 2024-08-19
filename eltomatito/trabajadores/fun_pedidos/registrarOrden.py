from conexionBD import *

class clientes:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def registrarcliente(self):
        try:
            cursor.execute(
                "INSERT INTO cliente (nombre) VALUES (%s)",
                (self.nombre,)
            )
            conexion.commit()
            print("Cliente registrado con éxito")
            return True
        except Exception as e:
            print(f"Error al registrar el cliente: {e}")
            return None

class pedido:
    def __init__(self, id_mesa, numero_mesa, numero_persona, num_orden, id_cliente, id_mesero):
        self.id_mesa = id_mesa
        self.numero_mesa = numero_mesa
        self.numero_persona = numero_persona
        self.num_orden = num_orden
        self.id_cliente = id_cliente
        self.id_mesero = id_mesero
        
    def registrarPedido(self):
        try:
            cursor.execute(
                "INSERT INTO pedido (id_mesa, numeroMesa, numeroPersonas, numOrden, id_cliente, id_mesero) VALUES (%s, %s, %s, %s, %s, %s)",
                (self.id_mesa, self.numero_mesa, self.numero_persona, self.num_orden, self.id_cliente, self.id_mesero)
            )
            conexion.commit()
            print("Pedido registrado con éxito")
            return True
        except Exception as e:
            print(f"Error al registrar el pedido: {e}")
            return None

class detalles:
    def __init__(self, id_pedido, id_categoria, id_platillo, cantidad):
        self.id_pedido = id_pedido
        self.id_categoria = id_categoria
        self.id_platillo = id_platillo
        self.cantidad = cantidad
        
    def registrardetalle(self):
        try:
            cursor.execute(
                "INSERT INTO detalles_pedido (id_pedido, id_categoria, id_platillo, cantidad) VALUES (%s, %s, %s, %s)",
                (self.id_pedido, self.id_categoria, self.id_platillo, self.cantidad)
            )
            conexion.commit()
            print("Detalle del pedido registrado con éxito")
            return True
        except Exception as e:
            print(f"Error al registrar el detalle del pedido: {e}")
            return None

