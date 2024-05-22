suma=0
num=1

while num>0:
    num=int(input("Ingrese un numero entero: "))
    
    if num>=10 and num<=30:
        suma+=num
        
print(f"La sumatoria total es: {suma}")

if suma>=500:
    print("Soy mayor a 500")
    
    

