from conexionBD import *
import tkinter as tk
from tkinter import messagebox, simpledialog

class AdministrarApp:
    def __init__(self, root):
        self.root = root

    @staticmethod
    def eliminiar_mesero():
        try:
            # Crear una nueva ventana para mostrar los resultados
            eliminar_window = tk.Toplevel()
            eliminar_window.title("Eliminar Mesero")

            # Consulta general
            query = "SELECT * FROM mesero ORDER BY id_mesero ASC;"
            cursor.execute(query)

            # Obtiene todos los resultados
            resultados = cursor.fetchall()

            # Muestra los resultados en la ventana
            result_text = tk.Text(eliminar_window, height=10, width=50)
            result_text.pack()
            for fila in resultados:
                result_text.insert(tk.END, f"{fila}\n")

            # Solicitar usuario del trabajador a eliminar
            usuario = simpledialog.askstring("Usuario", "Ingrese el usuario del trabajador a eliminar:")

            # Mostrar los datos actuales del mesero
            sql = "SELECT id_mesero, id_restaurante, nombres, apellidos, usuario, telefono FROM mesero WHERE usuario = %s"
            cursor.execute(sql, (usuario,))
            resultado = cursor.fetchone()

            if resultado:
                confirmar = messagebox.askquestion("Confirmación", f"¿Estás seguro de eliminar el siguiente registro?\n\n"
                                                f"id_mesero: {resultado[0]}\n"
                                                f"nombres: {resultado[2]}\n"
                                                f"apellidos: {resultado[3]}\n"
                                                f"usuario: {resultado[4]}\n"
                                                f"telefono: {resultado[5]}",
                                                icon='warning')

                if confirmar == "yes":
                    sql = "DELETE FROM mesero WHERE usuario = %s"
                    cursor.execute(sql, (usuario,))
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Registro eliminado correctamente")
                else:
                    messagebox.showinfo("Cancelado", "Eliminación del registro cancelado")
            else:
                messagebox.showerror("Error", "Usuario no encontrado")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error con el servidor... por favor intente más tarde.\n{e}")

        else:
            messagebox.showinfo("Éxito", "Ejecución realizada correctamente")

