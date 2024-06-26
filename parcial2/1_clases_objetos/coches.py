class Coches:

    # Constructor de la clase con parámetros para inicializar atributos
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    # Métodos o acciones o funciones que hace el objeto
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1   

# Crear un objeto o instancia de la clase
coche1 = Coches("Ferrari", "rojo", "2010", 300, 500, 2)

# Mostrar los valores iniciales del objeto o instancia de la clase
print(f"Marca: {coche1.marca} {coche1.color}, número de plazas: {coche1.plazas} \nModelo: {coche1.modelo} con una velocidad de {coche1.velocidad} Km/h y una potencia de {coche1.caballaje} hp")

# Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")

# Disminuir la velocidad del coche de 301 a 100
for i in range(1,202):
    coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")

# Crear un segundo coche con diferentes características
coche2 = Coches("BMW", "azul", "2015", 250, 400, 4)

# Mostrar los valores iniciales del segundo coche
print(f"\nMarca: {coche2.marca} {coche2.color}, número de plazas: {coche2.plazas} \nModelo: {coche2.modelo} con una velocidad de {coche2.velocidad} Km/h y una potencia de {coche2.caballaje} hp")

# Acelerar la velocidad del segundo coche de 250 a 251
coche2.acelerar()
print(f"La nueva velocidad del coche 2 es: {coche2.velocidad}")

# Disminuir la velocidad del segundo coche de 251 a 150
for i in range(1,102):
    coche2.frenar()

print(f"La nueva velocidad del coche 2 es: {coche2.velocidad}")
