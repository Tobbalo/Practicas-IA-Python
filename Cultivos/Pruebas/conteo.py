import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen_path = '4.jpg'
imagen = cv2.imread(imagen_path)

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro de mediana para reducir el ruido
imagen_filtrada = cv2.medianBlur(imagen_gris, 5)

# Aplicar umbral adaptativo para separar los objetos de interés
umbralizado = cv2.adaptiveThreshold(imagen_filtrada, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Encontrar contornos en la imagen umbralizada
contornos, _ = cv2.findContours(umbralizado, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filtrar los contornos para obtener solo los árboles (basado en el área)
area_minima = 1000  # Área mínima para considerar un contorno como árbol
contornos_arboles = [contorno for contorno in contornos if cv2.contourArea(contorno) > area_minima]

# Dibujar los contornos de los árboles en la imagen original
imagen_con_arboles = imagen.copy()
cv2.drawContours(imagen_con_arboles, contornos_arboles, -1, (0, 255, 0), 2)

# Contar los árboles detectados
numero_de_arboles = len(contornos_arboles)
print(f"Se han encontrado {numero_de_arboles} árboles.")

# Mostrar la imagen con los contornos de los árboles
plt.imshow(cv2.cvtColor(imagen_con_arboles, cv2.COLOR_BGR2RGB))
plt.title(f"Contornos de {numero_de_arboles} árboles")
plt.axis('off')
plt.show()
