class Figura():
    
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self._largo = largo
        self._ancho = ancho

    def get_largo(self):
        return self._largo

    def set_largo(self, nuevo_largo):
        self._largo = nuevo_largo

    def get_ancho(self):
        return self._ancho

    def set_ancho(self, nuevo_largo):
        self._ancho = nuevo_largo

    def calcular_area(self):
        return self._largo * self._ancho

class Circulo(Figura):
    def __init__(self, radio):
        self._radio = radio

    def get_radio(self):
        return self._radio

    def set_radio(self, nuevo_largo):
        self._radio = nuevo_largo

    def calcular_area(self):
        import math
        return math.pi * (self._radio ** 2)

class Triangulo(Figura):
    def __init__(self, altura, ancho):
        self._altura = altura
        self._ancho = ancho

    def get_altura(self):
        return self._altura

    def set_altura(self, nuevo_largo):
        self._altura = nuevo_largo

    def get_ancho(self):
        return self._ancho

    def set_ancho(self, nuevo_largo):
        self._ancho = nuevo_largo

    def calcular_area(self):
        return (self._ancho * self._altura) / 2