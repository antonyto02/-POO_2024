
#4.- Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado

n1 = int(input("Ingrese el primer número"))
n2 = int(input("Ingrese el segundo número"))

suma = n1+n2
resta = n1-n2
multiplicacion = n1*n2
division = n1/n2

print(f"Par los números {n1} y {n2} los resultados son los siguientes:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")