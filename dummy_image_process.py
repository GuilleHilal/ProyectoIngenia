from scipy import misc
from math import *
import random
import time
import math
import numpy as np
import matplotlib.pyplot as plt

imagen = 'estatico.png'
m_imagen = misc.imread(imagen)
m_plan = np.zeros((len(m_imagen[0]),len(m_imagen)))
print len(m_imagen)
print len(m_imagen[0])
for i in range(len(m_imagen)):
    for j in range(len(m_imagen[0])):
        #print m_imagen[i][j]
        if (m_imagen[i][j][0] == 254) and (m_imagen[i][j][1] == 254) and (m_imagen[i][j][2] == 254):
            m_plan[j][len(m_imagen)-1-i] = 0
        elif (m_imagen[i][j][0] > 230) and (m_imagen[i][j][1] < 80) and (m_imagen[i][j][2] < 80):
            inicio = [j,len(m_imagen)-1-i]
        elif (m_imagen[i][j][0] < 180) and (m_imagen[i][j][1] < 180) and (m_imagen[i][j][2] > 230):
            final = [j,len(m_imagen)-1-i]
        else:
            m_plan[j][len(m_imagen)-1-i] = 1

print m_imagen[151][172]

for i in range(len(m_plan)):
    print m_plan[i]
print inicio
print final

x_grid = []
y_grid = []
for i in range(len(m_plan)):
    for j in range(len(m_plan[0])):
        if (m_plan[i][j] == 1):
            y_grid.append(j)
            x_grid.append(i)
plt.plot(x_grid,y_grid,'ro')
plt.show()
