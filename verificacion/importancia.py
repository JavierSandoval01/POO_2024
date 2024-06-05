#VALIDACIÓN DE ENTRADAS

#Validar que la entrada de datos proporcionada por el usuario sea la necesitada.
#Si no se cumplen los requisitos pedir al usuario que ingrese el dato otra vez
#Hasta que se obtengan los datos esperados 

#ERROR al ingresar un tipo de dato diferente

numero_int=int(input("Ingrese un numero entero:"))

# Correos Electrónicos no valido
correo = input("Ingrese su correo electrónico: ")
print(f"Correo electrónico ingresado: {correo}")

#Contraseñas
contraseña = input("Ingrese su contraseña: ")
print("Contraseña ingresada.")



# Desbordamiento de Búfer
nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}!")

#Errores logicos de Formato/ Datos Inconsistentes
edad = int(input("Ingrese su edad: "))

#Error logico en operación matematica

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en cm: "))
imc = peso / ((altura/100) ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc}")

