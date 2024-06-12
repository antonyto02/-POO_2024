
# 3.- 

# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas



mi_lista = []

respuesta = "SI"
if not mi_lista:
    while respuesta == "SI":
        frase = input("Ingrese una palabra o frase: ")
        mi_lista.append(frase)
        respuesta = input("¿Desea agregar otra frase?(SI/NO)").upper()

for i in mi_lista:
    print(i.upper())

