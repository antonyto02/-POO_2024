paises = ["México", "USA", "Brasil", "China"]
numeros = [100,80,3.1416,75]
varios = ["UTD", True, 100, 0.100]

#Ordenar las listas
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#Agregar elementos

print(numeros)
numeros.append(100)
print(numeros)
numeros.insert(len(numeros),200)
print(numeros)


#Remover elementos

print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(4)
print(numeros)