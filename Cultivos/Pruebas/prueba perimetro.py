import matplotlib.pyplot as plt
import numpy as np

# Píxeles por metro (solo un valor de ejemplo)
PIXELS_PER_METER = 10

# Cargar la imagen
imagen_path = '2.jpg'
imagen = plt.imread(imagen_path)

# Crear una función para manejar los clics en la imagen
def onClick(event):
    if event.button == 1:
        puntos.append((event.xdata, event.ydata))
        ax.plot(event.xdata, event.ydata, 'ro')
        plt.draw()
        if len(puntos) >= 2:
            calcular_perimetro()
        if len(puntos) >= 3:
            dibujar_perimetro()

# Función para calcular la distancia euclidiana entre dos puntos
def distancia_entre_puntos(punto1, punto2):
    return np.sqrt((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)

# Función para calcular el perímetro en metros
def calcular_perimetro():
    perimetro = 0
    for i in range(len(puntos) - 1):
        perimetro += distancia_entre_puntos(puntos[i], puntos[i+1])
    perimetro += distancia_entre_puntos(puntos[-1], puntos[0])  # Cerrar el contorno
    perimetro_metros = perimetro / PIXELS_PER_METER
    print(f"El perímetro del contorno en metros es: {perimetro_metros:.2f} metros")

# Función para dibujar el perímetro en la imagen
def dibujar_perimetro():
    fig, ax = plt.subplots()
    ax.imshow(imagen)
    for i in range(len(puntos) - 1):
        ax.plot([puntos[i][0], puntos[i+1][0]], [puntos[i][1], puntos[i+1][1]], 'r-')
    ax.plot([puntos[-1][0], puntos[0][0]], [puntos[-1][1], puntos[0][1]], 'r-')
    plt.title("Perímetro del contorno")
    plt.axis('off')
    plt.show()

# Mostrar la imagen utilizando matplotlib
fig, ax = plt.subplots()
ax.imshow(imagen)
puntos = []

# Configurar el manejador de eventos de clic
fig.canvas.mpl_connect('button_press_event', onClick)

plt.title("Haz clic en los puntos del contorno. Cierra la ventana cuando termines.")
plt.show()

# Dibujar el contorno final en una única imagen
if len(puntos) >= 3:
    fig, ax = plt.subplots()
    ax.imshow(imagen)
    for i in range(len(puntos) - 1):
        ax.plot([puntos[i][0], puntos[i+1][0]], [puntos[i][1], puntos[i+1][1]], 'r-')
    ax.plot([puntos[-1][0], puntos[0][0]], [puntos[-1][1], puntos[0][1]], 'r-')
    plt.title("Perímetro del contorno final")
    plt.axis('off')
    plt.show()
