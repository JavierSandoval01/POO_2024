from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from conexionBD import conexion, cursor
from main import seleccionar_rol
from trabajadores.fun_pedidos.registrarOrden import clientes, pedido, detalles
import datetime

def menu_mesero(usuario):
    root = Tk()
    root.title("Menú Mesero")
    root.state('zoomed')
    root.configure(bg='black')

    numorden = 0
    fecha = datetime.datetime.now()
    id_pedido = None

    def abrir_menu_mesero():
        root.deiconify()
        root.state('zoomed')

    def tomar_orden():
        nonlocal numorden, id_pedido
        numorden += 1

        def registrar_orden():
            nonlocal id_pedido
            try:
                obj_cliente = clientes(nombre_cliente.get())
                resultado_cliente = obj_cliente.registrarcliente()
                
                if resultado_cliente:
                    id_cliente = cursor.lastrowid
                    
                    cursor.execute("SELECT id_mesero FROM mesero WHERE usuario = %s", (usuario,))
                    id_mesero = cursor.fetchone()[0]
                    
                    cursor.execute("SELECT id_mesa FROM mesa WHERE NumeroMesa = %s", (nu_mesa.get(),))
                    id_mesa = cursor.fetchone()[0]
                    
                    obj_pedido = pedido(id_mesa, int(nu_mesa.get()), int(nu_personas.get()), numorden, id_cliente, id_mesero)
                    resultado_pedido = obj_pedido.registrarPedido()
                    
                    if resultado_pedido:
                        id_pedido = cursor.lastrowid
                        ventana_orden.destroy()
                        tomar_pedido()
                    else:
                        messagebox.showerror("Error", "Hubo un error al registrar el pedido")
                else:
                    messagebox.showerror("Error", "Error al registrar el cliente")
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar la orden: {e}")

        def cancelar():
            ventana_orden.destroy()
            abrir_menu_mesero()

        root.withdraw()
        ventana_orden = Toplevel(root)
        ventana_orden.title("Tomar Pedido")
        ventana_orden.state('zoomed')
        ventana_orden.configure(bg='black')
        
        frame = Frame(ventana_orden, bg='black')
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        Label(frame, text="Número de mesa:", bg='black', fg='red', font=("Arial", 36)).grid(row=0, column=0, padx=20, pady=20)
        nu_mesa = Combobox(frame, values=[str(i) for i in range(1, 13)], font=("Arial", 36))
        nu_mesa.grid(row=0, column=1, padx=20, pady=20)
        nu_mesa.set("Seleccionar:")
        
        Label(frame, text="Número de personas:", bg='black', fg='red', font=("Arial", 36)).grid(row=1, column=0, padx=20, pady=20)
        nu_personas = Entry(frame, font=("Arial", 36))
        nu_personas.grid(row=1, column=1, padx=20, pady=20)
        
        Label(frame, text="Nombre del cliente:", bg='black', fg='red', font=("Arial", 36)).grid(row=2, column=0, padx=20, pady=20)
        nombre_cliente = Entry(frame, font=("Arial", 36))
        nombre_cliente.grid(row=2, column=1, padx=20, pady=20)
        
        Button(frame, text="Registrar", command=registrar_orden, font=("Arial", 36), bg='red', fg='white').grid(row=3, column=1, padx=20, pady=20)
        Button(frame, text="Cancelar", command=cancelar, font=("Arial", 36), bg='red', fg='white').grid(row=3, column=0, padx=20, pady=20)

    def tomar_pedido():
        def obtener_datos_categoria():
            cursor.execute("SELECT id_categoria, nombre FROM menu")
            categorias = cursor.fetchall()
            return {nombre: id_cat for id_cat, nombre in categorias}

        def obtener_datos_platillo(id_categoria):
            cursor.execute("SELECT id_platillo, tipo FROM platillo WHERE id_categoria = %s", (id_categoria,))
            platillos = cursor.fetchall()
            return {tipo: id_platillo for id_platillo, tipo in platillos}

        def agregar_detalle():
            opc_cat = cat_var.get()
            opc_platillo = platillo_var.get()
            
            if opc_cat == "Seleccionar categoría" or not opc_platillo:
                messagebox.showerror("Error", "Debe seleccionar una categoría y un platillo")
                return
            
            cantidad_str = cantidad_var.get()
            if not cantidad_str.isdigit():
                messagebox.showerror("Error", "La cantidad debe ser un número entero")
                return

            cantidad = int(cantidad_str)
            
            if cantidad <= 0:
                messagebox.showerror("Error", "La cantidad debe ser mayor a cero")
                return
            
            id_categoria = categorias.get(opc_cat)
            id_platillo = platillos_dict.get(opc_platillo)
            
            if id_categoria is None or id_platillo is None:
                messagebox.showerror("Error", "Categoría o platillo no válidos")
                return
            
            try:
                obj_detalles = detalles(id_pedido, id_categoria, id_platillo, cantidad)
                resultado_detalle = obj_detalles.registrardetalle()
                
                if resultado_detalle:
                    messagebox.showinfo("Éxito", "Detalle agregado correctamente")
                    platillo_var.set('')
                    cantidad_var.set('')
                else:
                    messagebox.showerror("Error", "Hubo un error al agregar el detalle")
            except Exception as e:
                messagebox.showerror("Error", f"Error al agregar el detalle: {e}")

        def finalizar_pedido():
            consulta = """
                SELECT p.numeroMesa, p.numeroPersonas, p.numOrden, m.nombre AS categoria, pl.tipo AS platillo, dp.cantidad, pl.precio, (dp.cantidad * pl.precio) AS subtotal 
                FROM pedido p 
                JOIN detalles_pedido dp ON p.id_pedido = dp.id_pedido 
                JOIN platillo pl ON dp.id_platillo = pl.id_platillo 
                JOIN menu m ON pl.id_categoria = m.id_categoria 
                WHERE p.id_pedido = %s
                """
            try:
                cursor.execute(consulta, (id_pedido,))
                resultados = cursor.fetchall()

                monto_total = 0
                ticket_text = f"Número de orden: {numorden}\n"
                for fila in resultados:
                    numero_mesa, numero_personas, num_orden, categoria, platillo, cantidad, precio, subtotal = fila
                    monto_total += subtotal
                    ticket_text += f"{categoria} de {platillo} - Cantidad: {cantidad} - Precio: ${precio:.2f} - Subtotal: ${subtotal:.2f}\n"

                ticket_text += f"\nMonto total: ${monto_total:.2f}"

                insertar_ticket = """
                INSERT INTO ticket (id_pedido, fecha, ImportePedido) 
                VALUES (%s, %s, %s)
                """
                cursor.execute(insertar_ticket, (id_pedido, fecha, monto_total))
                conexion.commit()

                messagebox.showinfo("Ticket", ticket_text)

                ventana_detalles.destroy()
                abrir_menu_mesero()
            except Exception as e:
                messagebox.showerror("Error", f"Error al finalizar el pedido: {e}")

        ventana_detalles = Toplevel(root)
        ventana_detalles.title("Agregar Detalle")
        ventana_detalles.state('zoomed')
        ventana_detalles.configure(bg='black')
        
        frame = Frame(ventana_detalles, bg='black')
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        categorias = obtener_datos_categoria()
        cat_var = StringVar()
        cat_var.set("Seleccionar categoría")
        Label(frame, text="Categoría:", bg='black', fg='red', font=("Arial", 36)).grid(row=0, column=0, padx=20, pady=20)
        cat_menu = Combobox(frame, textvariable=cat_var, font=("Arial", 36))
        cat_menu['values'] = ["Seleccionar categoría"] + list(categorias.keys())
        cat_menu.grid(row=0, column=1, padx=20, pady=20)
        
        platillo_var = StringVar()
        platillo_menu = Combobox(frame, textvariable=platillo_var, font=("Arial", 36))
        platillo_menu.grid(row=1, column=1, padx=20, pady=20)
        
        def actualizar_platillos(*args):
            nombre_categoria = cat_var.get()
            if nombre_categoria != "Seleccionar categoría":
                id_categoria = categorias.get(nombre_categoria)
                if id_categoria:
                    platillos = obtener_datos_platillo(id_categoria)
                    platillos_dict.update(platillos)
                    platillo_menu['values'] = list(platillos.keys())
                else:
                    platillo_menu['values'] = []

        cat_var.trace('w', actualizar_platillos)
        
        Label(frame, text="Platillo:", bg='black', fg='red', font=("Arial", 36)).grid(row=1, column=0, padx=20, pady=20)
        
        cantidad_var = StringVar()
        Label(frame, text="Cantidad:", bg='black', fg='red', font=("Arial", 36)).grid(row=2, column=0, padx=20, pady=20)
        cantidad_entry = Entry(frame, textvariable=cantidad_var, font=("Arial", 36))
        cantidad_entry.grid(row=2, column=1, padx=20, pady=20)
        
        Button(frame, text="Agregar detalle", command=agregar_detalle, font=("Arial", 36), bg='red', fg='white').grid(row=3, column=1, padx=20, pady=20)
        Button(frame, text="Finalizar pedido", command=finalizar_pedido, font=("Arial", 36), bg='red', fg='white').grid(row=4, column=1, padx=20, pady=20)

        platillos_dict = {}

    frame = Frame(root, bg='black')
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Button(frame, text="Tomar Orden", command=tomar_orden, font=("Arial", 36), bg='red', fg='white').pack(pady=50)
    Button(frame, text="Regresar", command=root.destroy, font=("Arial", 36), bg='red', fg='white').pack(pady=50)

    root.mainloop()

