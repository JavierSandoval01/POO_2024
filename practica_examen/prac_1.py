#Datos de un automovil, 


opc_otro="SI"
while opc_otro=="SI":
    opc=""
    cost_imp=0
    impuesto=0
    input("Ingrese la marca del automovil: ")
    costo=float(input("Ingrese el costo: "))
    print("Seleccione el origen del automovil \n [A] Alemania \n [B] Japon \n [C] Italia \n [D] USA ")
    while opc!="A" or opc!="B" or opc!="C" or opc!="D":
     opc=input()
     opc=opc.upper()
     if opc=="A":
        print ("El origen es Alemania")
        print (f"El impuesto a pagar es del 20%")
        impuesto=costo*(20/100)
        cost_imp=costo+impuesto
        print(f"Impuesto: {impuesto}")
        print(f"El costo con impuesto incluido es de: {cost_imp}")
        break
     elif  opc=="B":
        print ("El origen es Japon")
        print (f"El impuesto a pagar es del 30%")
        impuesto=costo*(30/100)
        cost_imp=costo+impuesto
        print(f"Impuesto: {impuesto}")
        print(f"El costo con impuesto incluido es de: {cost_imp}")
     elif  opc=="C":
        print ("El origen es Italia")
        print (f"El impuesto a pagar es del 15%")
        impuesto=costo*(15/100)
        cost_imp=costo+impuesto
        print(f"Impuesto: {impuesto}")
        print(f"El costo con impuesto incluido es de: {cost_imp}")
     elif  opc=="D":
        print ("El origen es USA")
        print (f"El impuesto a pagar es del 8%")
        impuesto=costo*(8/100)
        cost_imp=costo+impuesto
        print(f"Impuesto: {impuesto}")
        print(f"El costo con impuesto incluido es de: {cost_imp}")
     else:
        print("opcion no valida")
        opc=input("verifique: ")
    opc_otro=input("¿Desea calcular otro carro? [SI/NO]: ")
    opc_otro=opc_otro.upper()
  