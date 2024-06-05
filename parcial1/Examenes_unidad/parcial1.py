#Trabajadores
#4 semanas tiene un mes
opc="SI"
contador=0
suel_totales=0
while opc=="SI":
    sueldo_dia=0
    sueldo_semana=0
    nombre=input("Ingrese el nombre del trabajador: ")
    h_trab=int(input("Ingrese las horas trabajadas al dia: "))
    d_trab=int(input("Ingreser los dias trabajados a la semana: "))
    sueldo_h=int(input("Ingrese el sueldo por hora: "))
    
    sueldo_dia=h_trab*sueldo_h
    sueldo_semana=sueldo_dia*d_trab
    
    print(f"El sueldo que gana a la semana es: {sueldo_semana}")
    
    sueldo_mes=sueldo_semana*4
    
    print(f"El sueldo que gana al mes es de: {sueldo_mes}")
    
    if sueldo_mes<=10000:
        print("Obrero tipo A")
    elif sueldo_mes>10000 and sueldo_mes<15000:
        print("Obrero tipo B")
    else:
        print("Sin categoria")
    contador+=1
    
    suel_totales+=sueldo_mes
    
    opc=input("¿Desea ingresar otro trabajador? [SI/NO]")   
    opc=opc.upper() 
    while opc!="NO" and opc!="SI":
        opc=input("¿Desea ingresar otro trabajador? [SI/NO]")   
        opc=opc.upper() 
        if opc!="NO" and opc!="SI":
            print("Esa no es una opcion")

print(f"Trabajadores/pacientes capturados: {contador}")
print(f"Total de sueldos de todos los trabajadore: {suel_totales}")