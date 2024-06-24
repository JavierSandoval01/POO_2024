


salir=False

def suma(n1,n2):
    sum=n1+n2
    return sum

def resta(n1,n2):
    resta=n1-n2
    return resta

def multi(n1,n2):
    mult=n1*n2
    return mult

def division(n1,n2):
    divi=n1/n2
    return divi

while salir==False:
    print("_.::::::: CALCULADORA BASICA :::::::._\nSUMA[1]\nRESTA[2]\nMULTIPLICACION[3]\nDIVISION[4]\nSALIR[5]")
    opc=int(input("Seleccione una opcion: "))
    num1=int(input("Ingrese el num1: "))
    num2=int(input("Ingrese el num2: "))
    if opc==1:
        resultado_suma=suma(num1,num2)
        print(resultado_suma)
    elif opc==2:
        resultado_resta=resta(num1,num2)
        print(resultado_resta)
    elif opc==3:
       resultado_multi=multi(num1,num2)
       print(resultado_multi)
    elif opc==4:
        resultado_div=division(num1,num2)
        print(resultado_div)
    elif opc==5:
        salir=True
    else:
        print("Opcion no valida, verifique")    
