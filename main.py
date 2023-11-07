import matplotlib.pyplot as plt

# Definir las coordenadas de los vértices del cuadrado
x = [-1, -1, 1, 1, -1]  # Coordenadas x de los vértices
y = [-1, 1, 1, -1, -1]  # Coordenadas y de los vértices

# Crear el cuadrado
plt.plot(x, y, color='black')

#Crear un círculo con borde rojo y radio de 1
circulo = plt.Circle((0, 0), 1, edgecolor='red', facecolor='none')

# Agregar el círculo al gráfico
plt.gca().add_patch(circulo)

# Añadir un punto en coordenadas (0.5, 0.5) de color verde
plt.scatter(0.5, 0.5, color='green', s=50, label='Punto Verde')

# Establecer los límites de los ejes x e y
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# Mostrar el gráfico
plt.show()