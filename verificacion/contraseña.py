import re
 
 #crear contraseñas seguras
 #Longitud: Una contraseña debe tener al menos 12-16 caracteres.
 #Debe incluir una combinación de letras mayúsculas y minúsculas, números y caracteres especiales (por ejemplo, !, @, #, $, %, etc.).
 
while True:

    error=False
 
    #Solicitar datos
    usuario=input("Nombre de usuario ")
    pass1=input("Ingrese una contraseña: ")
    pass2=input("Repita la contraseña: ")
 
    #Validar contraseña
    
    #Validar longitud
    if len(pass1)<12:
        print("la longitud de la contraseña no es correcta")
        error=True

    #Validar que contenga al menos un numero
    if not re.search('[0-9]',pass1):
        print("la contraseña tiene que tener al menos un numero")
        error=True
        
    #Validar que contenga letras (minusculas)
    if not re.search('[a-z]', pass1):
        print("la contraseña tiene que tener al menos una letra")
        error=True

    #Validar que contenga letras (mayusculas)
    if not re.search('[A-Z]', pass1):
        print("la contraseña tiene que tener al menos una letra mayuscula")
        error=True
    #Validar caracteres especiales
    if not re.search('[!@#$%^&*(),.?":{}|<>]', pass1):
        print("la contraseña tiene que tener al menos un caracter especial")
        error=True
        
    #Verificar que las dos contraseñas sean iguales 
    if pass1!=pass2:
        print("las contrasenas no son iguales")
        error=True
    
    #Si todas las validaciones se cumplen aceptar la contraseña, de lo contrario, volver a pedirla.
    if error==False:
        print("OK")
        break
    
