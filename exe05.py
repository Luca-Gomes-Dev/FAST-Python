import numpy as np

# Dados de temperatura em graus Celsius (suponha que cada elemento representa uma temperatura)
temperaturas_celsius = np.array([25, 30, 15, 10, 35])

# Converter para Fahrenheit usando a fórmula: F = (C * 9/5) + 32
temperaturas_fahrenheit = (temperaturas_celsius * 9/5) + 32

# Converter para Kelvin usando a fórmula: K = C + 273.15
temperaturas_kelvin = temperaturas_celsius + 273.15

# Exibir os resultados
print("Temperaturas em Celsius:", temperaturas_celsius)
print("Temperaturas em Fahrenheit:", temperaturas_fahrenheit)
print("Temperaturas em Kelvin:", temperaturas_kelvin)
