# 4.- 

#  Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

lista = []
cadena = "Hola"
numero = 1
encendido = True

def tipo_dato():
    print("El tipo de dato de la variable lista es: ", type(lista))
    print("El tipo de dato de la variable cadena es: ", type(cadena))
    print("El tipo de dato de la variable numero es: ", type(numero))
    print("El tipo de dato de la variable encendido es: ", type(encendido))
          
tipo_dato()