import re
#Validación de la entrada de un Número Entero
while True:
    numero_int = input("Ingrese un numero entero: ")
    try:
        entero = int(numero_int)
        print("Si es un numero entero")
        print (f"Numero entero: {numero_int}")
        break
    except ValueError:
	    print("Lo que escribiste NO es un numero entero")
    

#Validación de la entrada de un Número Real
while True:
    numero_real = input("Ingrese un numero real: ")
    try:
        numero_real = float(numero_real)
        print("Si es un numero real")
        print (f"Numero real: {numero_real}")
        break
    except ValueError:
	    print("Lo que escribiste NO es un numero real")

#Validación de una Cadena sin Números
while True:
    cadena = input("Ingrese una cadena sin numeros")
    if  re.search('[0-9]',cadena):
        print("La cadena no debe contener números.")
    else:
        print ("Cadena valida")
        print(f"Cadena ingresada: {cadena}")
        break


    
