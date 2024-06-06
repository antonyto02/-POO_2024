"""
List (Array)
son colecciones o conjunto de datos/valores bajo 
un mismo nombre, para acceder a los valores se
hace con un índice numérico

Nota: sus valores sí son modificables

La lista es una colección ordenada y modificable. permite miembros
duplicados.


"""

# #Ejemplo 1 crear una lista con valores numericos enteros e imprimir la lista
# numeros=[23,34]
# print(numeros)


# #Recorrer la lista con for
# for i in numeros:
#     print(i)


# ##Recorrer la lista con un while 
# i=0
# while i<len(numeros):
#     print(numeros[i])
#     i+=1
encontrado = False
palabras = ["hola", "2024", "10.23", "True"]

palabra_buscar = input("Ingresa la palabra a buscar: ")


# for i in palabras:
#     if palabra_buscar==i:
#         print(f"Encontré la palabra {palabra_buscar}, en la posición: {palabras.index(i)}")
#         encontrado = True

# if encontrado == False: 
#     print(f"No se encontró la palabra dentro de la lista")


i = 0
encontrada = False

while i < len(palabras):
     if palabra_buscar==palabras[i]:
         print(f"Encontré la palabra {palabra_buscar}, en la posición: {i}")
         encontrada = True
         
     i += 1

if encontrada == False:
    print(f"No se encontró la palabra dentro de la lista")
