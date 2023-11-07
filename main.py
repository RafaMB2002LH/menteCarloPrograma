import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import randomCoordGenerator as rcg

if __name__=='__main__':
   
   # Definir las coordenadas de los vértices del cuadrado
   x = [-1, -1, 1, 1, -1]  # Coordenadas x de los vértices
   y = [-1, 1, 1, -1, -1]  # Coordenadas y de los vértices

   # Crear el cuadrado
   plt.plot(x, y, color='black')

   #Crear un círculo con borde rojo y radio de 1
   circulo = plt.Circle((0, 0), 1, edgecolor='red', facecolor='none')
   # Agregar el círculo al gráfico
   plt.gca().add_patch(circulo)

   # Lista para almacenar las coordenadas de los puntos
   coordenadas_puntos = []

   # Función para agregar un punto al gráfico y mantener los puntos anteriores
   def agregar_punto():
      x, y = rcg.randomCoordGenerator()
      coordenadas_puntos.append((x, y))
      puntos.set_offsets(coordenadas_puntos)

   # Crear el gráfico para los puntos
   puntos = plt.scatter([], [], color='blue', s=50, label='Puntos')
   plt.legend()

   # Establecer los límites de los ejes x e y
   plt.xlim(-2, 2)
   plt.ylim(-2, 2)

   # Función de animación que llama a la función para agregar un punto
   def animacion(frame):
      agregar_punto()

   # Crear la animación que llama a la función de animación
   anim = FuncAnimation(plt.gcf(), animacion, frames=100, repeat=False, interval=1000)

   # Mostrar el gráfico
   plt.show()  
