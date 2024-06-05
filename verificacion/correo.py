
import re
def validar_correo(arg_email):
    es_valido = True
    correo= re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    es_valido = False if not correo.match(arg_email) else True
    print("Email is valid" if es_valido else "Invalid email address.")


validar_correo("alvisonhunter@outlook.com") # This email address is valid
validar_correo("alvisondr.com") # missing an @
validar_correo("alvison@@peachtreelightscapes.com") # Double @ in the email
validar_correo("alvison.hunter@concentrixcom") # missing the dot

validar_correo(input("Ingrese su correo electronico: "))