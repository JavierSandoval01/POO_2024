# 5.- 
# Crear una lista y un diccionario con el contenido de esta tabla: 

#   ACCION              TERROR        DEPORTES
#   MAXIMA VELOCIDAD    LA MONJA       ESPN
#   ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION


#   imprimir la información

"""   

  Crear una lista y un diccionario con el contenido de esta tabla: 

  ACCION              TERROR        DEPORTES
  MAXIMA VELOCIDAD    LA MONJA       ESPN
  ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
  RAPIDO Y FURIOSO I  LA MALDICION   ACCION


  imprimir la información 

"""

listaProgramas=[
     ["ACCION","TERROR","DEPORTES"],
     ["MAXIMA VELOCIDAD","LA MONJA","ESPN"],
     ["ARMA MORTAL 4","EL CONJURO","MAS DEPORTE"],
     ["RAPIDO Y FURIOSO I","LA MALDICION","ACCION"]
   ]

for i in listaProgramas:
  print(i)

dictProgramas={
  "genero1":{"ACCION","TERROR","DEPORTES"},
  "genero2":{"MAXIMA VELOCIDAD","LA MONJA","ESPN"}
  
}

for i in dictProgramas:
  print(i)