#Manejo de errores es la forma en la que tienen los lenguajes de progrmación
#para evitar que sucedan errores en tiempo de ejecución

#Ejemplo 1 Error cuando una variable no se genera

# try:
#     nombre = input("Dame el nombre")

#     if len(nombre)>1:
#         nombre_usuario = "El nombre es: "+ nombre

#     print(nombre_usuario)
# except:
#     print("Es necesario introducir un nombre de usuario...")


#Ejemplo cuando se solicita un numero y se introduce una letra

# try:
#     numero = int(input("Dame un número: "))

#     if numero>0:
#         print("Soy un número entero positivo")
#     else:
#         print("Soy un número negativo")

# except:
#     print("No se puede convertir un caracter no numérico a número")
# else:
#     print("Todo correcto")

#Ejemplo 3 Cuando se generan múltiples excepciones

try:
    numero = int(input("Dame un número: "))

    print(f"El cuadrado  es: {numero*numero}")
except ValueError:
    print("Debes de introducir, un número no se puede convertir un caracter que no sea númerico")
except TypeError:
    print("No es posible convertir elel numero entero")
else:
    print("Finalizó correctamente")
finally:
    print("Listo, se terminó")

