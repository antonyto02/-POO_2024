#Concatenar cadenas de caracteres con contenido de variables

nombre = "Juan Antonio Delgado Rodríguez"
especialidad = "Área de Desarrollo de SW Multiplataforma"
carrera = "Ingeniero en Desarrollo y Gestión de Software"

#1er forma de concatenar
print("Mi nombre es: " + nombre + " estoy en la especialidad de: " + especialidad + " en la carrera de: " + carrera)
print("")

#2da forma de concatenar
print("Mi nombre es:", nombre, "estoy en la especialidad de:", especialidad, "en la carrera de:", carrera)
print("")

#3er forma de concatenar (La más común)
print(f"Mi nombre es: {nombre} estoy en la especialidad de: {especialidad} en la carrera de: {carrera}")
print("")

#4ta forma de concatenar
print("Mi nombre es: {} estoy en la especialidad de: {} en la carrera de: {}".format(nombre,especialidad,carrera))
print("")

#5ta forma de concatenar
print('Mi nombre es: ' + nombre + ' estoy en la especialidad de: ' + especialidad + ' en la carrera de: ' + carrera)