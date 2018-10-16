from scipy import misc
from math import *
import random
import time
import math
import plan
import time
import numpy as np
import matplotlib.pyplot as plt
#Necesitas descargar la libreria motionless que es la que uso para la imagen png
#Esta libreria usa la API de google maps para crear mapas estaticos
import requests
from motionless import DecoratedMap, LatLonMarker

#Defino las latitudes y longitudes de origen y destino...
latorigen = -31.438459
longorigen = -64.202148
latdestino = -31.441901
londestino = -64.199753

#Creo el mapa del tipo y zoom que elija. La key la modifique desde la clase DecoratedMap
#Lo mejor seria que bajes vos la libreria y modifiques la key aca abajo, cuando crees la clase.
#La key la pones como atributo cuando la creas key=claveTuya
road_styles = [ { 'feature': 'road.highway','element': 'geomoetry','rules': {'visibility': 'off','color': '#c280e9'} }
              , { 'feature': 'transit.line','rules': {'visibility': 'simplified','color': '#bababa'}}
              , { 'feature': 'road', "element": "labels.text", "rules": { "visibility": "off" } }
              , { 'feature': 'poi', "element" : "labels.text","rules": { "visibility": "off" } }
              , { 'feature': 'poi', "rules": { "visibility": "off" } }
              , { 'feature': 'landscape', "element" : "labels.text","rules": { "visibility": "off" } } 
              , { 'feature': 'transit', "element" : "labels.text","rules": { "visibility": "off" } }
              , { 'feature': 'administrative', "element" : "labels.text","rules": { "visibility": "off" } } ]

dmap = DecoratedMap(style=road_styles,maptype='roadmap', zoom=15, key=None)

#Agrego los marcadores
dmap.add_marker(LatLonMarker(latorigen, longorigen, label='O',color='blue'))
dmap.add_marker(LatLonMarker(latdestino, londestino, label='D'))

#Genero la URL desde donde se descarga la imagen...
url = dmap.generate_url()

#Creo la imagen...
f=open('estatico.png','wb')
f.write(requests.get(url).content)
f.close()

# Abrir imagen (por ahora van a ser dos tareas separadas)
imagen = 'estatico.png'
m_imagen = misc.imread(imagen)
m_plan = np.zeros((len(m_imagen[0]),len(m_imagen)))
print len(m_imagen)
print len(m_imagen[0])

# Obtener puntos de interes
for i in range(len(m_imagen)):
    for j in range(len(m_imagen[0])):
        #print m_imagen[i][j]
        if (m_imagen[i][j][0] == 254) and (m_imagen[i][j][1] == 254) and (m_imagen[i][j][2] == 254):
            m_plan[j][len(m_imagen)-1-i] = 0
        elif (m_imagen[i][j][0] > 230) and (m_imagen[i][j][1] < 180) and (m_imagen[i][j][2] < 180):
            inicio = [j,len(m_imagen)-1-i]
            m_plan[j][len(m_imagen)-1-i] = 0
        elif (m_imagen[i][j][0] < 180) and (m_imagen[i][j][1] < 180) and (m_imagen[i][j][2] > 230):
            final = [j,len(m_imagen)-1-i]
            m_plan[j][len(m_imagen)-1-i] = 0
        else:
            m_plan[j][len(m_imagen)-1-i] = 1

#for i in range(len(m_plan)):
#    print m_plan[i]

# Procesamiento de punto de inicio y final para que no quede encerrado

SIZE_MARK = 10

for i in range(SIZE_MARK):
    for j in range(SIZE_MARK):
        m_plan[inicio[0]+SIZE_MARK/2-i][inicio[1]+SIZE_MARK-j] = 0
        m_plan[final[0]+SIZE_MARK/2-i][final[1]+SIZE_MARK-j] = 0
        
path = plan.plan(m_plan,inicio,final)
path.astar()
path.smooth(0.5,0.15)

path_hard = path.path

#print inicio
#print final
#print path_hard

plt.plot(np.array(path_hard)[:,0],np.array(path_hard)[:,1],'bo')

x_grid = []
y_grid = []
for i in range(len(m_plan)):
    for j in range(len(m_plan[0])):
        if (m_plan[i][j] == 1):
            y_grid.append(j)
            x_grid.append(i)
plt.plot(x_grid,y_grid,'ro')
plt.show()
