"""
comentario de varias lineas
Nota: A la hora de concatenae cadenas no es posible incluir en
algunas ocasiones contenido de variables que no sean del tipo de dato str

"""

#Comentario de una linea

#Concatenar un str con str
texto="Soy una cadena de texto"

numero=23

print(texto + "y soy otra cadena")

#Concatenar un int con str

numero=23
numero_str=str(numero)
print("El numero:" + numero_str)

print("El numero:" + str(numero))

#Concatenar un str con int

n1="23"
n2=33

suma=int(n1)+n2

print("El número: "+str(suma))

#Concatenar un float y int con str

n1="23"
n2=33.0

suma=int(n1)+n2

print("El número: "+str(suma))
print(f"El número: {suma}")

#Concatenar un float y int con str

n1="23.34"
n2="33.99"

suma=float(n1)+float(n2)

print(f"El número: {suma}")