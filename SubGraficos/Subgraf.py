# -*- coding: utf-8 -*-

'''
Iván Rodríguez - 2018
Código generado para el canal de YouTube Piensa 3D
'''

# Importamos los módulos necesarios
import math
import numpy as np
from matplotlib import pyplot as plt

# Generamos los datos para el gráfico
x = np.array(range(500))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])

# Generamos un segundo conjunto de datos para el gráfico
x_2 = np.array(range(500))*0.1
y_2 = np.zeros(len(x_2))
for j in range(len(x_2)):
    y_2[j] = math.cos(x_2[j])

# Creamos el gráfico
plt.subplot(221)
plt.plot(x,y,'--')
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Representacion de funciones 1")
plt.subplot(222)
plt.plot(x_2,y_2,'*')
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Representacion de funciones 2")
plt.subplot(223)
plt.plot(x,y,'o')
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Representacion de funciones 3 ")
plt.subplot(224)
plt.plot(x_2,y_2,'-')
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Representacion de funciones 4")

plt.show()
