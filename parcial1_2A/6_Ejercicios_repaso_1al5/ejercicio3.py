#3.- Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

for i in range(1,61,1):
    print(f"El cuadrado de {i} es: {i*i}")

i = 1
while i <= 60:
    print(f"El cuadrado de {i} es: {i*i}")
    i += 1