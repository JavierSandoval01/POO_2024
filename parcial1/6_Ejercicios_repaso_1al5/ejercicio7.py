#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario
impar=0
tipo=""
num1=int(input("Ingrese el primer numero (inicio del rango): "))
num2=int(input("Ingrese el segundo numero: (fin del rango): "))

for i in range(num1+1,num2):
    impar=i%2
   
    if impar > .1:
        print(i)
