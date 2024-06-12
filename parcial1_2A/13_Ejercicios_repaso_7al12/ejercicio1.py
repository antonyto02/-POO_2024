#Ejercicio 1

#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado


numeros = [12,2,34,5,65,6,97,98]


def recorrer():
    for i in numeros:
        print(i)

def string():
    cadena = ""
    for i in numeros:
        i = str(i)
        cadena = cadena+i
    print(cadena)

def ordenar():
    numeros.sort()
    for i in numeros:
        print(i)

def longitud():
    print(f"La longitud de la lista es {len(numeros)}")

def buscar():
    num = int(input("Ingrese un número: "))
    if num in numeros:
        for i,j in enumerate(numeros):
            if j == num:
              print(f"El número {num} se encontró en la posición {i}")
              break
    else:
        print(f"No se encontró el numero{num}")


print("a) Recorrer la lista")
print("b) Convertir a cadena la lista")
print("c) Ordenar la lista")
print("d) Longitud la lista")
print("e) Buscar en la lista")
opcion = input("¿Qué desea hacer?")



if opcion == "a":
    recorrer()
elif opcion == "b":
    string()
elif opcion == "c":
    ordenar()
elif opcion == "d":
    longitud()
elif opcion == "e":
    buscar()
else:
    print("Opción no válida")











