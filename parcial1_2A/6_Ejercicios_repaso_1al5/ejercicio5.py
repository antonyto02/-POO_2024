#5.- Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

n1 = int(input("Ingrese el primer número (límite inferior)"))
n2 = int(input("Ingrese el segundo número (límite superior)"))

i = n1+1
while i < n2:
    print(i)
    i += 1
