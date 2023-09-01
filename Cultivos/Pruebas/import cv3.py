import cv2
import numpy as np

# Cargar la imagen
ruta_imagen = 'arbol.jpg'
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

# Dibujar los contornos en la imagen original y contar árboles
numero_arboles = 0
for contorno in contornos:
    area = cv2.contourArea(contorno)
    if area > 100:  # Puedes ajustar este umbral según tu imagen
        perimetro = cv2.arcLength(contorno, True)
        approx = cv2.approxPolyDP(contorno, 0.02 * perimetro, True)
        if len(approx) >= 3:  # Considerar solo contornos con al menos 3 vértices
            cv2.drawContours(imagen, [approx], -1, (0, 255, 0), 2)
            numero_arboles += 1

# Guardar la imagen con los contornos y árboles detectados
nombre_salida = 'deteccion_arboles.jpg'
cv2.imwrite(nombre_salida, imagen)

# Mostrar el número de árboles detectados
print(f"Se han detectado {numero_arboles} árboles en la imagen. Imagen guardada como {nombre_salida}.")
