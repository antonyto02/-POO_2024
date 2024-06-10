# Ejemplo de funciones lambda

# Una función lambda simple que toma un argumento
duplicar = lambda x: x * 2
print(duplicar(5))  # Salida: 10

# Una función lambda que toma dos argumentos
sumar = lambda x, y: x + y
print(sumar(2, 3))  # Salida: 5

# Una función lambda que no toma argumentos
saludar = lambda: "¡Hola, Mundo!"
print(saludar())  # Salida: ¡Hola, Mundo!

# Usando una función lambda como función de orden superior
numeros = [1, 2, 3, 4, 5]
numeros_cuadrados = list(map(lambda x: x ** 2, numeros))
print(numeros_cuadrados)  # Salida: [1, 4, 9, 16, 25]

# Usando una función lambda como filtro
numeros = [1, 2, 3, 4, 5]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)  # Salida: [2, 4]

# Usando una función lambda como reducctor
from functools import reduce
numeros = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)  # Salida: 120