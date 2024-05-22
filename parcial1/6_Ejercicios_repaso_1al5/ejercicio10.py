# Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron
cont_rep=0
cont_apr=0

for i in range (1,16):
    cal=float(input(f"Ingrese la calificacion [{i}]: "))
    if cal>=8:
        cont_apr+=1
    else:
        cont_rep+=1

print(f"Alumnos aprobados: {cont_apr}")
print(f"Alumnos reprobados: {cont_rep}")