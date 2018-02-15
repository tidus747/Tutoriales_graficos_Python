# -*- coding: utf-8 -*-

'''
Iván Rodríguez - 2017
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
plt.ion()
plt.plot(x,y,'bo',x_2,y_2,'y-')

#Colocamos las etiquetas de los ejes
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")

#Colocamos la leyenda
plt.legend(['Seno','Coseno'])

#Colocamos el título del gráfico
plt.title("Representacion de funciones")
