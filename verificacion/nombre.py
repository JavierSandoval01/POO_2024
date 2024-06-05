import re



while True:
    error=False
    nombre = input("Ingrese un nombre: ")
    # Verificar que el nombre contenga solo letras y no supere el máximo de caracteres
    if not re.search("^[a-zA-Z ]*$", nombre):
        print("Nombre inválido. El nombre DEBE contener solo letras.")
        error=True
    if not len(nombre) <= 35: 
        print("Nombre inválido. El nombre DEBE tener máximo 35 caracteres.")
        error=True
    if error==False:
        print("Nombre valido")
        break
