"""

    Existe una estructura de condición llamada "if"
    la cual evalua una condición para encontrar el valor "True" y si se cumple
    la condición se ejecuta la line o lineas de código

    Tenemos 4 variantes del if

    1.- if simple
    1.- if compuesto
    1.- if anidado
    1.- if y elif

"""

#Ejemplo 1 if simple

color = input("Ingresa un color: ")

if color =="rojo":
    print("Soy el color rojo")

#Ejemplo 2 if compuesto

color = input("Ingresa un color: ")

if color =="rojo":
    print("Soy el color rojo")
else:
    print("No soy el color rojo")


#Ejemplo 3 if anidado

color = input("Ingresa un color: ")

if color =="rojo":
    print("Soy el color rojo")
    if color !="rojo":
        print("No soy el color rojo")
else:
    print("No soy el color rojo, soy otra cosa")

#Ejemplo 3 if anidado

color = input("Ingresa un color: ")

if color =="rojo":
    print("Soy el color rojo")
elif color == "amarillo":
    print("Soy el color amarillo")
elif color == "azul":
    print("Soy el color azul")
elif color == "morado":
    print("Soy el color morado")
else:
    print("No soy ninguna de las anteriores")

#Ejemplo 4 Crear un programa que solicite el día de la semana
# e imprima en pantalla el día que le corresponde

dia = int(input("Ingrese el número de día de la semana(1-7): "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Lunes")
elif dia == 3:
    print("Martes")
elif dia == 4:
    print("Miércoles")
elif dia == 5:
    print("Jueves")
elif dia == 6:
    print("Viernes")
elif dia == 7:
    print("Sábado")
else:
    print("No es un dia válido")
    