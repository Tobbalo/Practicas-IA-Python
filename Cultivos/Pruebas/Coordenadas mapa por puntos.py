import matplotlib.pyplot as plt

# Cargar la imagen
imagen_path = '1.jpeg'
imagen = plt.imread(imagen_path)

# Crear una función para manejar los clics en la imagen
def onClick(event):
    if event.button == 1:
        puntos.append((event.xdata, event.ydata))
        ax.plot(event.xdata, event.ydata, 'ro')
        plt.draw()

# Mostrar la imagen utilizando matplotlib
fig, ax = plt.subplots()
ax.imshow(imagen)
puntos = []

# Configurar el manejador de eventos de clic
fig.canvas.mpl_connect('button_press_event', onClick)

plt.title("Haz clic en los puntos del contorno. Cierra la ventana cuando termines.")
plt.show()

# Mostrar las coordenadas de los puntos dibujados
print("Coordenadas de los puntos:")
for punto in puntos:
    print(punto)
