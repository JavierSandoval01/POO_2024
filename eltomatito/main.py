import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from trabajadores.login import *
from trabajadores.mesero import *
from funciones import *
from trabajadores.administrar import *

def iniciar_sesion():
    rol = selector_rol.get()
    usuario = entry_usuario.get()
    password = entry_password.get()

    login_func = login_admin if rol == "Administrador" else login_mesero
    menu_func = menu_administrar if rol == "Administrador" else menu_mesero

    if login_func(usuario, password):
        messagebox.showinfo("Acceso", f"Acceso concedido\nBienvenido, {rol}: {usuario}")
        ventana.destroy()  # Cierra la ventana de inicio de sesión
        menu_func(usuario)  # Abre la ventana del menú correspondiente
    else:
        messagebox.showerror("Error", "Acceso denegado")

def seleccionar_rol():
    global ventana
    ventana = tk.Tk()
    ventana.title("El Tomatito")
    ventana.geometry("800x800")  # Tamaño inicial de la ventana
    ventana.configure(bg="#0e0e0e")
    
    # Maximizar la ventana
    ventana.state('zoomed')

    # Crear un marco con borde rojo
    marco = tk.Frame(
        ventana,
        bg="#010006",
        bd=2,  # Grosor del borde interno
        relief="solid",
        highlightbackground="red",  # Color del borde
        highlightthickness=4  # Grosor del borde externo
    )
    marco.place(relx=0.5, rely=0.5, anchor="center", width=700, height=900)  # Centra el marco

    # Intentar cargar la imagen
    tk.Label(marco, text="Bienvenido al sistema gestor", font=("Arial", 18), fg="white", bg="black").pack(pady=20)
   
    imagen = Image.open("logo1.jpg").resize((700, 200), Image.LANCZOS)  # Ajustar tamaño de la imagen
    logo = ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(marco, image=logo, bg="black")
    label_imagen.image = logo
    label_imagen.pack(pady=20)
    
    tk.Label(marco, text="Iniciar sesión", font=("Arial", 18), fg="red", bg="black").pack(pady=20)
    
    global selector_rol
    selector_rol = Combobox(marco, values=["Administrador", "Mesero"], state="readonly", font=("Arial", 14))
    selector_rol.set("Selecciona un rol")
    selector_rol.pack(pady=10)

    global entry_usuario
    tk.Label(marco, text="Usuario", font=("Arial", 16), fg="white", bg="black").pack(pady=10)
    entry_usuario = tk.Entry(marco, width=30, font=("Arial", 14))
    entry_usuario.pack(pady=10)

    global entry_password
    tk.Label(marco, text="Contraseña", font=("Arial", 16), fg="white", bg="black").pack(pady=10)
    entry_password = tk.Entry(marco, show="*", width=30, font=("Arial", 14))
    entry_password.pack(pady=10)

    tk.Button(marco, text="Iniciar sesión", width=25, font=("Arial", 14), command=iniciar_sesion, bg="red", fg="white").pack(pady=20)

    ventana.mainloop()

if __name__ == "__main__":
    seleccionar_rol()
