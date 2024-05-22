 # Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for
#
cuadrado=0
contador=1

while contador<60:
    cuadrado=contador^2
    print(f"{contador}^2={cuadrado}")
    contador+=1

cuadrado=0
contador=1

for i in range(1,61):
    cuadrado=i*i
    print(f"{i}^2={cuadrado}")