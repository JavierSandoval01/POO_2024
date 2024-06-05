#Pedir datos
#Validar peso y altura para que no existan diviciones entre 0
#Calcular el imc
while True: 
    try:
        peso = float(input("Ingrese su peso en kg: "))
        if peso<=0:
            print("Ingrese un peso valido, Mayor a 0")
        else:
            break
    except ValueError:
	    print("Ingrese un peso valido, no letras")
    
while True:
    try:
        altura = float(input("Ingrese su altura en cm: "))
        if altura<=0:
            print("Ingrese una altura valida, Mayor a 0")
        else:
            break
    except ValueError:
        print("Ingrese una altura valida, no letras")


imc = peso / ((altura/100) ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc}")
