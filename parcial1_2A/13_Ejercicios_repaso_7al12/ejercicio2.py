# 2.- 
# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

lista_while = []
valor = 1
while len(lista_while) < 120:
    lista_while.append(valor)
    valor += 1
print("Lista creada con while:", lista_while)


print("\nUsando un bucle for:")
lista_for = []
for i in range(1, 121):
    lista_for.append(i)
print("Lista creada con for:", lista_for)
