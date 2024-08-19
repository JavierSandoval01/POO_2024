import hashlib
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
from conexionBD import *
from trabajadores.administracionbd.platillos import *



def menu_administrar(usuario):
    root = tk.Tk()
    app = AdministrarApp(root)
    root.mainloop()

class AdministrarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Administración")
        self.root.configure(bg='black')  # Cambia el color de fondo a negro
        self.root.state('zoomed')  # Maximiza la ventana principal
        self.current_window = None  # Para rastrear la ventana secundaria abierta
        self.menu_administrar()

    def menu_administrar(self):
        self.clear_window()
        tk.Label(text="Opciones de administrador", font=("Arial", 40), fg="red", bg="black").pack(pady=10)
        tk.Label(text="", font=("Arial", 16), fg="white", bg="black").pack(pady=10)
        tk.Button(self.root, text="Administrar usuarios",width=25, font=("Arial", 14), command=self.administrar_usuarios).pack()
        tk.Label(text="", font=("Arial", 16), fg="white", bg="black").pack(pady=10)
        tk.Button(self.root, text="Administrar menú",width=25, font=("Arial", 14), command=self.administrar_menu).pack()
        tk.Label(text="", font=("Arial", 16), fg="white", bg="black").pack(pady=10)
        tk.Button(self.root, text="Salir de administración",width=25, font=("Arial", 14), command=self.root.quit).pack()

    def administrar_usuarios(self):
        self.clear_window()
        tk.Label(text="//Administrar usuarios//", font=("Arial", 40), fg="red", bg="black").pack(pady=10)

        tk.Button(self.root, text="Agregar un nuevo usuario", width=25,font=("Arial", 14),command=self.agregar_usuario).pack()
        tk.Label(text="", font=("Arial", 20), fg="white", bg="black").pack(pady=10)
        tk.Button(self.root, text="Eliminar un usuario mesero",width=25,font=("Arial", 14), command=self.eliminar_mesero).pack()
        tk.Label(text="", font=("Arial", 20), fg="white", bg="black").pack(pady=10)
        tk.Button(self.root, text="Volver",width=25,font=("Arial", 14), command=self.menu_administrar).pack()

    def agregar_usuario(self):
        self.clear_window()
        tk.Label(self.root,font=("Arial", 20), text="//Agregar usuario//",fg="red", bg="black").pack()

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)

        self.rol_var = tk.StringVar(value="Seleccionar:")
        self.nombres_var = tk.StringVar()
        self.apellidos_var = tk.StringVar()
        self.usuario_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.telefono_var = tk.StringVar()

        tk.Label(form_frame,font=("Arial", 20), text="Rol:").grid(row=0, column=0, padx=10, pady=5)
        rol_menu = ttk.Combobox(form_frame,font=("Arial", 20), textvariable=self.rol_var, values=["Administrador", "Mesero"])
        rol_menu.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame,font=("Arial", 20), text="Nombres:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(form_frame, textvariable=self.nombres_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame,font=("Arial", 20), text="Apellidos:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(form_frame, textvariable=self.apellidos_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame,font=("Arial", 20), text="Usuario:").grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(form_frame, textvariable=self.usuario_var).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(form_frame,font=("Arial", 20), text="Contraseña:").grid(row=4, column=0, padx=10, pady=5)
        tk.Entry(form_frame, textvariable=self.password_var, show='*').grid(row=4, column=1, padx=10, pady=5)

        tk.Label(form_frame,font=("Arial", 20), text="Teléfono:").grid(row=5, column=0, padx=10, pady=5)
        tk.Entry(form_frame, textvariable=self.telefono_var).grid(row=5, column=1, padx=10, pady=5)

        tk.Button(self.root,font=("Arial", 20), text="Registrar Usuario", command=self.registrar_usuario).pack(pady=20)
        tk.Button(self.root,font=("Arial", 20), text="Volver", command=self.administrar_usuarios).pack()

    def registrar_usuario(self):
        rol = self.rol_var.get()
        nombres = self.nombres_var.get()
        apellidos = self.apellidos_var.get()
        usuario = self.usuario_var.get()
        password = self.password_var.get()
        telefono = self.telefono_var.get()

        if not (nombres and apellidos and usuario and password and telefono):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        obj_persona = None
        if rol == "Administrador":
            obj_persona = administradores(nombres, apellidos, usuario, password, telefono)
        elif rol == "Mesero":
            obj_persona = meseros(nombres, apellidos, usuario, password, telefono)
        else:
            messagebox.showerror("Error", "Rol no válido")
            return

        if obj_persona:
            resultado = obj_persona.registrarpersona()

            if resultado:
                messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
            else:
                messagebox.showerror("Error", "Hubo un error al registrar el usuario")
        else:
            messagebox.showerror("Error", "No se pudo crear el objeto persona")

        self.administrar_usuarios()
        

    def eliminar_mesero(self):
        self.clear_window()
        tk.Label(self.root,font=("Arial", 20), text="//Eliminar Mesero//",fg="red", bg="black").pack()

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)

        self.usuario_var = tk.StringVar()

        tk.Label(form_frame,font=("Arial", 20), text="Seleccionar Mesero:").grid(row=0, column=0, padx=10, pady=5)

        self.usuario_combobox = ttk.Combobox(form_frame, textvariable=self.usuario_var)
        self.usuario_combobox.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(self.root,font=("Arial", 20), text="Eliminar Mesero", command=self.confirmar_eliminacion).pack(pady=20)
        tk.Button(self.root,font=("Arial", 20), text="Volver", command=self.administrar_usuarios).pack()

        self.cargar_meseros()

    def cargar_meseros(self):
        try:
            query = "SELECT usuario FROM mesero ORDER BY usuario ASC;"
            cursor.execute(query)
            resultados = cursor.fetchall()

            usuarios = [resultado[0] for resultado in resultados]
            self.usuario_combobox['values'] = usuarios

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al cargar los usuarios: {e}")

    def confirmar_eliminacion(self):
        usuario = self.usuario_var.get()

        if not usuario:
            messagebox.showerror("Error", "Debe seleccionar un mesero")
            return

        try:
            sql = "SELECT id_mesero, nombres, apellidos, telefono FROM mesero WHERE usuario = %s"
            cursor.execute(sql, (usuario,))
            resultado = cursor.fetchone()

            if resultado:
                confirmar = messagebox.askquestion("Confirmación", f"¿Estás seguro de eliminar el siguiente registro?\n\n"
                                                            f"id_mesero: {resultado[0]}\n"
                                                            f"nombres: {resultado[1]}\n"
                                                            f"apellidos: {resultado[2]}\n"
                                                            f"telefono: {resultado[3]}",
                                                            icon='warning')

                if confirmar == "yes":
                    sql = "DELETE FROM mesero WHERE usuario = %s"
                    cursor.execute(sql, (usuario,))
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Mesero eliminado correctamente")
                    self.cargar_meseros()  # Actualizar la lista de meseros
                else:
                    messagebox.showinfo("Cancelado", "Eliminación del mesero cancelada")

            else:
                messagebox.showerror("Error", "Usuario no encontrado")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error con el servidor... por favor intente más tarde.\n{e}")

    def administrar_menu(self):
        self.clear_window()
        
        tk.Label(self.root, text="//Administrar platillos//",font=("Arial", 40),bg="black", fg="red").pack()
        tk.Label(text="", font=("Arial", 20), fg="white", bg="black").pack(pady=10)
        tk.Label(text="", font=("Arial", 20), fg="white", bg="black").pack(pady=10)
        tk.Button(self.root, text="Agregar un nuevo platillo",width=25, font=("Arial", 14), command=self.agregar_platillo).pack()
        tk.Label(text="", font=("Arial", 20), fg="white", bg="black").pack(pady=10)
        tk.Button(self.root, text="Modificar platillos",width=25, font=("Arial", 14), command=self.modificar_platillo).pack()
        tk.Label(text="", font=("Arial", 20), fg="white", bg="black").pack(pady=10)
        tk.Button(self.root, text="Eliminar platillos",width=25, font=("Arial", 14), command=self.eliminar_platillo).pack()
        tk.Label(text="", font=("Arial", 20), fg="white", bg="black").pack(pady=10)
        tk.Button(self.root, text="Volver",width=25, font=("Arial", 14), command=self.menu_administrar).pack()

    def agregar_platillo(self):
        self.clear_window()
        tk.Label(self.root,font=("Arial", 20), text="//Agregar platillo//",fg="red", bg="black").pack()

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)

        self.tipo_var = tk.StringVar()
        self.precio_var = tk.DoubleVar()
        self.categoria_var = tk.StringVar()

        tk.Label(form_frame, font=("Arial", 20),text="Nombre del platillo:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(form_frame, textvariable=self.tipo_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame,font=("Arial", 20), text="Precio:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(form_frame, textvariable=self.precio_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame,font=("Arial", 20), text="Categoría:").grid(row=2, column=0, padx=10, pady=5)
        self.categoria_combobox = ttk.Combobox(form_frame, textvariable=self.categoria_var)
        self.categoria_combobox.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.root,font=("Arial", 20), text="Registrar Platillo", command=self.registrar_platillo).pack(pady=20)
        tk.Button(self.root,font=("Arial", 20), text="Volver", command=self.administrar_menu).pack()

        self.cargar_categorias()

    def cargar_categorias(self):
        try:
            query = "SELECT nombre FROM menu ORDER BY nombre ASC;"
            cursor.execute(query)
            resultados = cursor.fetchall()

            categorias = [resultado[0] for resultado in resultados]
            self.categoria_combobox['values'] = categorias

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al cargar las categorías: {e}")

    def registrar_platillo(self):
        tipo = self.tipo_var.get()
        precio = self.precio_var.get()
        nombre_categoria = self.categoria_var.get()

        if not (tipo and precio and nombre_categoria):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            query = "SELECT id_categoria FROM menu WHERE nombre = %s"
            cursor.execute(query, (nombre_categoria,))
            resultado = cursor.fetchone()

            if resultado:
                id_categoria = resultado[0]
            else:
                messagebox.showerror("Error", "Categoría no válida")
                return

            sql = "INSERT INTO platillo (tipo, id_categoria, precio) VALUES (%s, %s, %s)"
            cursor.execute(sql, (tipo, id_categoria, precio))
            conexion.commit()
            messagebox.showinfo("Éxito", "Platillo registrado exitosamente")
            self.administrar_menu()

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al registrar el platillo: {e}")

    def modificar_platillo(self):
        self.clear_window()
        tk.Label(self.root, text="//Modificar Platillo//",fg="red", bg="black",font=25).pack()

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)

        self.tipo_var = tk.StringVar()
        self.precio_var = tk.DoubleVar()
        self.categoria_var = tk.StringVar()
        self.id_platillo_var = tk.StringVar()

        tk.Label(form_frame, text="Categoría:").grid(row=0, column=0, padx=10, pady=5)
        self.categoria_combobox = ttk.Combobox(form_frame, textvariable=self.categoria_var)
        self.categoria_combobox.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame,font=("Arial", 20), text="ID Platillo:").grid(row=1, column=0, padx=10, pady=5)
        self.id_platillo_combobox = ttk.Combobox(form_frame, textvariable=self.id_platillo_var)
        self.id_platillo_combobox.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame,font=("Arial", 20), text="Tipo:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(form_frame,font=("Arial", 20), textvariable=self.tipo_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame,font=("Arial", 20), text="Precio:").grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(form_frame, textvariable=self.precio_var).grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.root,font=("Arial", 20), text="Modificar Platillo", command=self.actualizar_platillo).pack(pady=20)
        tk.Button(self.root,font=("Arial", 20), text="Volver", command=self.administrar_menu).pack()

        self.cargar_categorias()
        self.categoria_combobox.bind("<<ComboboxSelected>>", self.actualizar_platillos)

    def cargar_platillos(self, categoria):
        try:
            query = """SELECT id_platillo, tipo 
                       FROM platillo 
                       WHERE id_categoria = (SELECT id_categoria FROM menu WHERE nombre = %s) 
                       ORDER BY id_platillo ASC;"""
            cursor.execute(query, (categoria,))
            resultados = cursor.fetchall()

            platillos = [f"{resultado[0]} - {resultado[1]}" for resultado in resultados]
            self.id_platillo_combobox['values'] = platillos
            if platillos:
                self.id_platillo_combobox.set(platillos[0])  # Seleccionar el primer id por defecto

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al cargar los platillos: {e}")

    def actualizar_platillos(self, event=None):
        categoria = self.categoria_var.get()
        if categoria:
            self.cargar_platillos(categoria)

    def actualizar_platillo(self):
        id_platillo = self.id_platillo_var.get().split(" - ")[0]  # Extraer solo el ID
        tipo = self.tipo_var.get()
        precio = self.precio_var.get()
        nombre_categoria = self.categoria_var.get()

        if not (id_platillo and tipo and precio and nombre_categoria):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            query = "SELECT id_categoria FROM menu WHERE nombre = %s"
            cursor.execute(query, (nombre_categoria,))
            resultado = cursor.fetchone()

            if resultado:
                id_categoria = resultado[0]
            else:
                messagebox.showerror("Error", "Categoría no válida")
                return

            sql = "UPDATE platillo SET tipo = %s, id_categoria = %s, precio = %s WHERE id_platillo = %s"
            cursor.execute(sql, (tipo, id_categoria, precio, id_platillo))
            conexion.commit()
            messagebox.showinfo("Éxito", "Platillo actualizado exitosamente")
            self.administrar_menu()

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar el platillo: {e}")

    def eliminar_platillo(self):
        self.clear_window()
        tk.Label(self.root,font=("Arial", 20), text="//Eliminar Platillo//",fg="red", bg="black").pack()

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)

        self.categoria_var = tk.StringVar()
        self.id_platillo_var = tk.StringVar()

        tk.Label(form_frame,font=("Arial", 20), text="Categoría:").grid(row=0, column=0, padx=10, pady=5)
        self.categoria_combobox = ttk.Combobox(form_frame, textvariable=self.categoria_var)
        self.categoria_combobox.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame,font=("Arial", 20), text="ID Platillo:").grid(row=1, column=0, padx=10, pady=5)
        self.id_platillo_combobox = ttk.Combobox(form_frame, textvariable=self.id_platillo_var)
        self.id_platillo_combobox.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(self.root,font=("Arial", 20), text="Eliminar Platillo", command=self.confirmar_eliminacion_platillo).pack(pady=20)
        tk.Button(self.root,font=("Arial", 20), text="Volver", command=self.administrar_menu).pack()

        self.cargar_categorias()
        self.categoria_combobox.bind("<<ComboboxSelected>>", self.actualizar_platillos)

    def confirmar_eliminacion_platillo(self):
        id_platillo = self.id_platillo_var.get().split(" - ")[0]  # Extraer solo el ID

        if not id_platillo:
            messagebox.showerror("Error", "Debe ingresar el ID del platillo")
            return

        try:
            sql = "SELECT tipo, precio, id_categoria FROM platillo WHERE id_platillo = %s"
            cursor.execute(sql, (id_platillo,))
            resultado = cursor.fetchone()

            if resultado:
                tipo, precio, id_categoria = resultado
                confirmar = messagebox.askquestion("Confirmación", f"¿Estás seguro de eliminar el siguiente registro?\n\n"
                                                                f"Tipo: {tipo}\n"
                                                                f"Precio: {precio}\n"
                                                                f"ID Categoría: {id_categoria}",
                                                                icon='warning')

                if confirmar == "yes":
                    sql = "DELETE FROM platillo WHERE id_platillo = %s"
                    cursor.execute(sql, (id_platillo,))
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Platillo eliminado correctamente")
                    self.cargar_platillos(self.categoria_var.get())  # Actualizar la lista de platillos
                else:
                    messagebox.showinfo("Cancelado", "Eliminación del platillo cancelada")

            else:
                messagebox.showerror("Error", "Platillo no encontrado")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error con el servidor... por favor intente más tarde.\n{e}")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()