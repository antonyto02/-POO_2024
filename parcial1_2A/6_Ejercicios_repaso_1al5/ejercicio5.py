#5.- Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

n1 = int(input("Ingrese el primer número (límite inferior)"))
n2 = int(input("Ingrese el segundo número (límite superior)"))

for i in range(n1+1,n2,1):
    print(i)
