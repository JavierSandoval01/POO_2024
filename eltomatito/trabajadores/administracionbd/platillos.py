import tkinter as tk
from tkinter import simpledialog, messagebox
from conexionBD import cursor, conexion
import hashlib

# Clase para agregar platillos
class AgregarPlatillos:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def registrarplatillo(self):
        try:
            cursor.execute(
                "INSERT INTO platillo (tipo, id_categoria, precio) VALUES (%s, %s, %s)",
                (self.nombre, self.categoria, self.precio)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return None

# Función para eliminar un platillo
def eliminar_platillo(root):
    cat = simpledialog.askinteger("Categoría", "Ingrese la categoría a la que pertenece el platillo a eliminar:", parent=root)
    
    def mostrar_platillos_por_categoria(id_categoria_seleccionada):
        query = "SELECT id_platillo, tipo, precio FROM platillo WHERE id_categoria = %s;"
        cursor.execute(query, (id_categoria_seleccionada,))
        platillos = cursor.fetchall()
        platillos_str = "\n".join([f"ID: {p[0]}, Tipo: {p[1]}, Precio: {p[2]}" for p in platillos])
        messagebox.showinfo("Platillos", f"Platillos en la categoría {id_categoria_seleccionada}:\n\n{platillos_str}", parent=root)

    mostrar_platillos_por_categoria(cat)

    id_platillo_a_eliminar = simpledialog.askinteger("ID Platillo", "Ingrese el ID del platillo que desea eliminar:", parent=root)

    cursor.execute("SET foreign_key_checks = 0;")
    query_eliminar = "DELETE FROM platillo WHERE id_platillo = %s;"
    cursor.execute(query_eliminar, (id_platillo_a_eliminar,))
    conexion.commit()
    cursor.execute("SET foreign_key_checks = 1;")

    messagebox.showinfo("Eliminado", f"El platillo con ID {id_platillo_a_eliminar} ha sido eliminado.", parent=root)

# Función para modificar un platillo
def modificar_platillo(root):
    cat = simpledialog.askinteger("Categoría", "Ingrese la categoría a la que pertenece el platillo a modificar:", parent=root)
    
    def mostrar_platillos_por_categoria(id_categoria_seleccionada):
        query = "SELECT id_platillo, tipo, precio FROM platillo WHERE id_categoria = %s;"
        cursor.execute(query, (id_categoria_seleccionada,))
        platillos = cursor.fetchall()
        platillos_str = "\n".join([f"ID: {p[0]}, Tipo: {p[1]}, Precio: {p[2]}" for p in platillos])
        messagebox.showinfo("Platillos", f"Platillos en la categoría {id_categoria_seleccionada}:\n\n{platillos_str}", parent=root)

    mostrar_platillos_por_categoria(cat)

    id_platillo_a_modificar = simpledialog.askinteger("ID Platillo", "Ingrese el ID del platillo que desea modificar:", parent=root)

    nuevo_tipo = simpledialog.askstring("Nuevo Tipo", "Ingrese el nuevo tipo de platillo (o deje en blanco para mantener el actual):", parent=root)
    nuevo_precio = simpledialog.askstring("Nuevo Precio", "Ingrese el nuevo precio del platillo (o deje en blanco para mantener el actual):", parent=root)

    query_actualizar = "UPDATE platillo SET "
    valores = []
    
    if nuevo_tipo:
        query_actualizar += "tipo = %s, "
        valores.append(nuevo_tipo)
    
    if nuevo_precio:
        query_actualizar += "precio = %s, "
        valores.append(nuevo_precio)
    
    query_actualizar = query_actualizar.rstrip(", ")
    query_actualizar += " WHERE id_platillo = %s;"
    valores.append(id_platillo_a_modificar)

    cursor.execute(query_actualizar, tuple(valores))
    conexion.commit()

    messagebox.showinfo("Modificado", f"El platillo con ID {id_platillo_a_modificar} ha sido actualizado.", parent=root)

# Clase principal de la aplicación
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrar Platillos")
        self.root.configure(bg='black')  # Fondo negro
        self.root.geometry('600x400')

        # Botones para registrar, modificar y eliminar platillos
        self.center_and_style_buttons(self.root, "Registrar platillo", self.registrar_platillo)
        self.center_and_style_buttons(self.root, "Modificar platillo", lambda: modificar_platillo(self.root))
        self.center_and_style_buttons(self.root, "Eliminar platillo", lambda: eliminar_platillo(self.root))

    def registrar_platillo(self):
        nombre = simpledialog.askstring("Nombre", "Ingrese el nombre del platillo:", parent=self.root)
        categoria = simpledialog.askinteger("Categoría", "Ingrese la categoría del platillo:", parent=self.root)
        precio = simpledialog.askfloat("Precio", "Ingrese el precio del platillo:", parent=self.root)

        platillo = AgregarPlatillos(nombre, categoria, precio)
        if platillo.registrarplatillo():
            messagebox.showinfo("Éxito", "Platillo registrado exitosamente.", parent=self.root)
        else:
            messagebox.showerror("Error", "No se pudo registrar el platillo.", parent=self.root)

    def center_and_style_buttons(self, parent, text, command):
        button = tk.Button(parent, text=text, fg="white", bg="red", font=("Arial", 18), command=command)
        button.pack(pady=20)

# Clases para manejar administradores y meseros
class administradores:
    def __init__(self, nombres, apellidos, usuario, password, telefono):
        self.nombres = nombres
        self.apellidos = apellidos
        self.usuario = usuario
        self.contrasena = self.hash_password(password)
        self.telefono = telefono
        
    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()
    
    def registrarpersona(self):
        try:
            cursor.execute(
                "insert into administrador values(null,1,%s,%s,%s,%s,%s)",
                (self.nombres, self.apellidos, self.usuario, self.contrasena, self.telefono)
            )
            conexion.commit()
            return True
        except:
            return None
            
class meseros:
    def __init__(self, nombres, apellidos, usuario, password, telefono):
        self.nombres = nombres
        self.apellidos = apellidos
        self.usuario = usuario
        self.contrasena = self.hash_password(password)
        self.telefono = telefono
        
    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()
    
    def registrarpersona(self):
        try:
            cursor.execute(
                "insert into mesero values(null,1,%s,%s,%s,%s,%s)",
                (self.nombres, self.apellidos, self.usuario, self.contrasena, self.telefono)
            )
            conexion.commit()
            return True
        except:
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
