#Validar numero telefonico / México

#Longitud Adecuada: un número de teléfono válido tiene 10 dígitos, excluyendo el código de área.
#Formato Correcto: solo números

import re


while True:

    error=False
    
    #Solicitar numero de telefono
    num_tel=str(input("Ingrese su numero telefonico: "))
   
 
    
    #Validar longitud
    if not len(num_tel)==10:
        print("la longitud del número telefonico no es correcta")
        error=True

   
    #Validar que no contenga letras 
    patron = r"^[0-9]*$"
    if not re.search(patron, num_tel):
        
        print("El número de telefono solo debe contener numeros")
        error=True
    #Si todas las validaciones se cumplen aceptar la contraseña, de lo contrario, volver a pedirla.
    if error==False:
        print("OK")
        break