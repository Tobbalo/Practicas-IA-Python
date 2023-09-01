import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
ruta_imagen = '1.jpg'
imagen = cv2.imread(ruta_imagen)

# Convertir la imagen a espacio de color HSV
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Definir un rango de colores que corresponden a los árboles (por ejemplo, tonos verdes)
rango_bajo = np.array([30, 40, 40])
rango_alto = np.array([90, 255, 255])

# Crear una máscara usando el rango de colores
mascara = cv2.inRange(hsv, rango_bajo, rango_alto)

# Aplicar operaciones morfológicas para mejorar la detección
kernel = np.ones((5, 5), np.uint8)
mascara = cv2.erode(mascara, kernel, iterations=1)
mascara = cv2.dilate(mascara, kernel, iterations=2)

# Encontrar contornos en la máscara
contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Calcular la transformada de distancia
dist_transform = cv2.distanceTransform(mascara, cv2.DIST_L2, 5)
_, dist_thresh = cv2.threshold(dist_transform, 0.1 * dist_transform.max(), 255, 0)
dist_thresh = np.uint8(dist_thresh)

# Encontrar los contornos de los árboles individuales
contornos, _ = cv2.findContours(dist_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en la imagen original y contar árboles
numero_arboles = 0
for contorno in contornos:
    if cv2.contourArea(contorno) > 10000:  # Puedes ajustar este umbral según tu imagen
        cv2.drawContours(imagen, [contorno], -1, (0, 255, 0), 2)
        numero_arboles += 1
# Mostrar la imagen con matplotlib
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Detección de árboles')
plt.axis('off')
plt.show()

print(f"Se han detectado {numero_arboles} árboles en la imagen.")
