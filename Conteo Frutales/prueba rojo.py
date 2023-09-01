import cv2
import numpy as np

# Cargar una imagen en formato BGR
img_bgr = cv2.imread("apple.jpg")

# Convertir la imagen BGR a HSV
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

# Definir los límites inferiores y superiores del rango de color rojo en HSV
# Rango 1: rojo claro (0 a 30 y 150 a 180)
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([30, 255, 255])
# Rango 2: rojo oscuro (330 a 360)
lower_red2 = np.array([150, 100, 100])
upper_red2 = np.array([180, 255, 255])

# Crear máscaras para cada rango de color rojo
mask_red1 = cv2.inRange(img_hsv, lower_red1, upper_red1)
mask_red2 = cv2.inRange(img_hsv, lower_red2, upper_red2)

# Combinar las máscaras para obtener una única máscara que cubra ambos rangos de rojo
mask_red = cv2.bitwise_or(mask_red1, mask_red2)

# Aplicar la máscara a la imagen original para obtener solo los píxeles rojos
img_red = cv2.bitwise_and(img_bgr, img_bgr, mask=mask_red)

# Mostrar la imagen original y la imagen solo con los píxeles rojos
cv2.imshow("Imagen original", img_bgr)
cv2.imshow("Píxeles rojos", img_red)
cv2.waitKey(0)
cv2.destroyAllWindows()
