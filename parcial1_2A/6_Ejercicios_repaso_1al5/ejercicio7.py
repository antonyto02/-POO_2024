#7.- Hacer un programa que muestre todos los 
#numeros impares entre 2 numeros que decida el usuario

n1 = int(input("Ingrese el primer número(límite inicial)"))
n2 = int(input("Ingrese el segundo número(límite final)"))

for i in range(n1+1,n2,1):
    if i%2 != 0:
        print(i)

