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
# encontrado = False
# palabras = ["hola", "2024", "10.23", "True"]

# palabra_buscar = input("Ingresa la palabra a buscar: ")


# for i in palabras:
#     if palabra_buscar==i:
#         print(f"Encontré la palabra {palabra_buscar}, en la posición: {palabras.index(i)}")
#         encontrado = True

# if encontrado == False: 
#     print(f"No se encontró la palabra dentro de la lista")


# i = 0
# encontrada = False

# while i < len(palabras):
#      if palabra_buscar==palabras[i]:
#          print(f"Encontré la palabra {palabra_buscar}, en la posición: {i}")
#          encontrada = True
         
#      i += 1

# if encontrada == False:
#     print(f"No se encontró la palabra dentro de la lista")

# Ejemplo 3 Lista multilinea o multidimensional (matriz) para crear una agenda


# agenda=[
#     ["Juan","6181234567"],
#     ["Alfonso","6187654321"],
#     ["Dago","8002002200"]
#     ["Medrano","5624996522"]
#     ]
# print(agenda)
# for i in agenda:
#     print (f"{agenda.index(i)+1} .- {i}")

# #ejemplo 4 Crear un programa que permita gestionar películas, colocar un menú de opciones para
# #agregar, remover, consultar películas.
# #Notas
# # 1.- Utilizar funciones y mandar llamar desde otro archivo
# # 2.- Utilizar listas para almacenar los nombres de películas

# def insertarPeliculas():
#     pelicula = input("Ingrese la película")
#     peliculas.append(pelicula)
#     espereTecla()

# def eliminarPeliculas():
#     pelicula = input("Ingrese la película a eliminar")
#     if pelicula in peliculas:
#         peliculas.remove(pelicula)
#         print("Película eliminada")
#     else:
#         print("Película no encontrada")
#     espereTecla()

# def consultar peliculas():
# for i in peliculas:
#     print(f"{peliculas.index(i)+1}.- {i}")
#     espereTecla()



# peliculas=[]

# print("\n\t..::: CINÉPOLIS CLON :::... \n 1.- Agregar \n 2.- Eliminar \n 3.- Consultar \n 4.- SALIR \n 5.- SALIR ") 
# opcion=input("\t Elige una opción: ").upper()

# if opcion == "1" or opcion == "AGREGAR":
#     agregar_pelicula()
# elif opcion == "2" or opcion == "ELIMINAR":
#     eliminar_pelicula()
# elif opcion == "3" or opcion == "CONSULTAR":
#     consultar_peliculas()


    