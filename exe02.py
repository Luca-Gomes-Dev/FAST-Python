import numpy as np


temperaturas = np.array([28.5, 29.0, 27.8, 26.5, 30.2, 31.5, 29.8])

temperatura_media = np.mean(temperaturas)


temperatura_maxima = np.max(temperaturas)


temperatura_minima = np.min(temperaturas)


print(f"Temperatura média: {temperatura_media :.2f}°C")
print(f"Temperatura máxima: {temperatura_maxima}°C")
print(f"Temperatura mínima: {temperatura_minima}°C")
