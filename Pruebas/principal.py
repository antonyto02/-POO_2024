# principal.py
import sys
import os

# Agrega el directorio actual al PATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from funciones import saludo, suma

# Llamamos a las funciones importadas
print(saludo())  # Debería imprimir: Hola, ¿cómo estás?
print(suma(5, 3))  # Debería imprimir: 8