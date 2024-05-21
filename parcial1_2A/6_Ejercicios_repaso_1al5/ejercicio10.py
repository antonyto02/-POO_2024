#10.- Crear un programa que solicite la calificacion de 15 alumnos
# e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

alumnos_reprobados = 0
alumnos_aprobados = 0


for i in range(1,16,1):
    calificacion = int(input(f"Ingrese la calificación del alumno {i}"))
    if calificacion < 80:
        alumnos_reprobados += 1
    else:
        alumnos_aprobados += 1

print(f"El número de alumnos aprobados fue de {alumnos_aprobados}")
print(f"El número de alumnos reprobados fue de {alumnos_reprobados}")