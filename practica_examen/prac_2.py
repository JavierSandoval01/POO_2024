#IMC
opc=""
while opc!="NO":
    imc=0
    print("calcular el IMC")

    peso=float(input("Ingrese su peso: "))
    estatura=float(input("Ingrese su estatura: "))

    print(f"Su peso es: {peso}")
    print(f"Su estatura es: {estatura}")

    imc= peso/(estatura*estatura)
    print(f"Su IMC es: {imc}")

    if imc<18.50:
        print("Conposicion corporal: Peso inferior al normal")
    elif imc>18.50 and imc<24.99 :
        print("Conposicion corporal: normal")
    elif imc>25.00 and imc<29.99:
        print("Conposicion corporal: Peso superior al normal")
    elif imc>30:
        print("Conposicion corporal: obesidad")
    opc=input("Quiere calcular otro IMC? [SI/NO]")
    opc=opc.upper()
