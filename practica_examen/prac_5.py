#datos de un trabajador
opc="SI"
while opc!="NO":
    edad=int(input("Ingrese la edad del trabajador"))
    nombre=input("Ingrese el  nombre del trabajador: \n hola ")
    h_trab=float(input("Ingrese las horas trabajadas: "))
    h_sueldo=float(input("Ingrese el sueldo por hora"))
    
    if h_trab==10:
        aumento=20
    elif h_trab==15:
        aumento=30
        
    
