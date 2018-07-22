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

# Creamos el gráfico
plt.plot(x,y)

#Colocamos las etiquetas de los ejes
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")

#Colocamos el título del gráfico
plt.title("Representacion de funciones")

#Colocamos texto en el gráfico
plt.text(0,0,"Texto 1",fontsize=40)

plt.show()
