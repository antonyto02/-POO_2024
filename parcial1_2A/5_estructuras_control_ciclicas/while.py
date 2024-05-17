#El Ciclo While es una Estrcutura iterativa que se ejecuta X veces siempre y 
#cuando la condición se cumpla y se seguirá ejecutando tantas veces como se
#True la condición

# Sintaxis
#  while condicion:
#   bloque de instrucciones

#Ejemplo 1 Crear un programa que imprima en pantalla 5 veces
#el @

contador = 3

for contador in range (1,6,1):
    print("@")

#Ejemplo 2 Crear un programa que imprima los números del 1 al 5 y los sume y al final imprima la suma

suma = 0

for contador in range (1,6,1):
    print(contador)
    suma = suma+contador
print(f"La suma es: {suma}")

#Ejemplo 3 Crear un programa que imprima de multiplicar que el usuario desee

n = int(input("Ingrese el número de la tabla deseada"))

for i in range (1,11,1):
    print(f"{n} X {i} = {n*i}")