# 1.- 

#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

#Lista con 8 numeros enteros
lista_numeros=[8,2,6,4,5,3,7,1]

#  a.- Recorrer la lista y mostrarla

for i in lista_numeros:
    print((i))

#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
def rec_num():
 for valor in lista_numeros:
    print(str(valor))

rec_num()
#  c.- ordenarla y mostrarla
lista_numeros.sort()
print(lista_numeros)

#  d.- mostrar su longitud

print(len(lista_numeros))

#  e.- buscar algun elemento que el usuario pida por teclado

palabra__buscar=input("Ingresa la palabra a buscar: ")
encontro=False
 for i in lista_numeros:    
     if i == palabra__buscar:
         print(f"Se encontro la palabra {palabra__buscar} a buscar en a la posicion {palabras.index(i)}")
         encontro=True
