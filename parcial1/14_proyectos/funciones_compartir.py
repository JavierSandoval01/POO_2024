peliculas=[]

def borrarPantalla():
  import os  
  os.system("clear")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def agregarPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  pelicula=input("Ingresa el nombre: ")
  peliculas.append(pelicula)

def eliminarPeliculas():
  borrarPantalla()
  print(".:: Baja de Peliculas ::. ")
  pelicula=input("Ingresa el nombre: ")
  i=0
  encontro=False
  while i<len(peliculas):
    if peliculas[i]==pelicula:
      print(f"La pelicula es: {pelicula}")
      cambio=input("¿Deseas eliminar la pelicula (SI/NO): ?").upper()
      if cambio=="SI":
         peliculas.remove(pelicula)
      encontro=True 
    i+=1    
      
  if not encontro:
    print("La pelicula NO existe, no es posible eliminar")   

def consultarPeliculas():
   print(f"Las peliculas actuales: {peliculas}")

def buscarPeliculas():
  borrarPantalla()
  print(".:: Buscar una Peliculas ::. ")
  pelicula=input("Ingresa el nombre: ")
  encontro=False 
  i=0
  while i<len(peliculas):
    if peliculas[i]==pelicula:
      print(f"La pelicula es: {pelicula}")
      encontro=True 
    i+=1    
      
  if not encontro:
    print("La pelicula NO existe")  

def actualizarPeliculas():
  borrarPantalla()
  print(".:: Actualizar Peliculas ::. ")
  pelicula=input("Ingresa el nombre: ")
  i=0
  encontro=False
  while i<len(peliculas):
    if peliculas[i]==pelicula:
      print(f"La pelicula es: {pelicula}")
      cambio=input("¿Deseas cambiar el nombre (SI/NO): ?").upper()
      if cambio=="SI":
        pelicula=input("Ingresa el nuevo nombre: ")
        peliculas[i]=pelicula
      encontro=True 
    i+=1    
      
  if not encontro:
    print("La pelicula NO existe, no es posible actualizar")     

def vaciarPeliculas():
  peliculas.clear()
  return "Lista Vacia"
###### funciones de calculadora  #######
import math

# x = math.sqrt(2)

# print(x)

# y=math.pow(2,3)

# print(y)

def solicitarDatos():
   n1=int(input("Numero #1: "))
   n2=int(input("Numero #2: "))
   return n1,n2

def solicitarDato():
   n1=int(input("Numero #1: "))
   return n1   
   
def getCalculadora(num1,num2,operacion):
    if operacion=="1" or operacion=="+" or operacion=="SUMA":
        return f"{num1}+{num2}={int(num1)+int(num2)}"
    elif operacion=="2" or operacion=="-" or operacion=="RESTA":
        return f"{num1}-{num2}={int(num1)-int(num2)}"  
    elif operacion=="3" or operacion=="*" or operacion=="MULTIPLICACION":
        return f"{num1}*{num2}={int(num1)*int(num2)}"        
    elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
        return f"{num1}/{num2}={int(num1)/int(num2)}" 
    elif operacion=="5" or operacion=="POTENCIA":
        return f"{num1} elevado a {num2} = {math.pow(int(num1),int(num2))}"  
    elif operacion=="6" or operacion=="RAIZ":
        return f"Raiz de {num1} = {math.sqrt(int(num1))}"       
    else:
        return "Opción invalida por favor vuelve a intentarlo"          