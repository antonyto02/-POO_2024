# 6.- Mostrar todas las tablas del 1 al 10. 
# Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
for i in range (1,11,1):
    print(f"Tabla de multiplicar del {i}")
    for j in range(1,11,1):
        print(f"{i} X {j} = {i*j}")
