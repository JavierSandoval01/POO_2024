

#### VALIDAR parametros de edad

validar_edad=False
while validar_edad==False:
    try:
        edad=int(input("Ingrese una edad valida: "))
    except ValueError:
        print("Debes escribir un número.")
        continue
    if edad<=0 or edad>150:
        print("Edad no valida")
        continue
    else:
        validar_edad=True
        print("Edad valida")