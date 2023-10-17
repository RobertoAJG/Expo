import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Crear datos para la superficie
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Trazar la superficie 3D
surface = ax.plot_surface(x, y, z, cmap='viridis')

# Configurar etiquetas de ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

ax.set_title('Superficie 3D')

# Agregar una barra de color
fig.colorbar(surface, shrink=0.5, aspect=5)

# Mostrar la gráfica
plt.show() 

